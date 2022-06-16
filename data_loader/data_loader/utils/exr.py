import OpenEXR
import Imath
import array
import numpy as np
import time

from typing import List, Tuple

class EXRFile(object):
    def __init__(self, verbose : int = 0) -> None:
        self.verbose = verbose # 0 for no display, 1 for all displays
        super().__init__()

    def open(self, exr_filename : str, channels : List[Tuple], channels_output_names : List[str]) -> dict:
        if self.verbose == 1 :
            print("Opening EXR file : " + exr_filename )
            t0 = time.time()

        if len(channels) != len(channels_output_names):
            raise ValueError("Number of channels not matching the given output names")
        
        data = dict()

        file = OpenEXR.InputFile(exr_filename)
        
        # Compute the image size
        file_header = file.header()
        dw = file.header()['dataWindow']
        w, h = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)

        # Read the channels as 32-bit floats
        PIXELTYPE = Imath.PixelType(Imath.PixelType.FLOAT)

        # Load each requested channel
        for i, channel_tuple in enumerate(channels):
            data_channel = [array.array('f', file.channel(Chan, PIXELTYPE)).tolist() for Chan in channel_tuple]

            np_array_channel  = np.zeros((h,w, len(channel_tuple)), np.float32)

            for j, channel in enumerate(channel_tuple):
                ch_np_array_channel = np.zeros((h,w), np.float32)
                ch_np_array_channel[:,:] = np.array(data_channel[j]).reshape(ch_np_array_channel.shape[0],-1)
                np_array_channel[:, :, j] = ch_np_array_channel
            
            data[channels_output_names[i]] = np_array_channel

        if self.verbose == 1 :
            t1 = time.time()
            print("Loading time EXR file : " + str(t1-t0) )
        return data
            