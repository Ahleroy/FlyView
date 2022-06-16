import re
import numpy as np
import sys
import time

class PFMFile(object):

    def __init__(self, verbose = 0) -> None:
        self.data = None
        self.verbose = verbose
    def read(self, filename):
        """
        Read PFM files
        From : https://github.com/liruoteng/OpticalFlowToolkit
        MIT Licence
        """
        if self.verbose == 1 :
            t0 = time.time()

        file = open(filename, 'rb')

        color = None
        width = None
        height = None
        scale = None
        endian = None

        header = file.readline().rstrip()

        if header == b'PF':
            color = True
        elif header == b'Pf':
            color = False
        else:
            raise Exception('Not a PFM file.')

        dim_match = re.match(rb'^(\d+)\s(\d+)\s$', file.readline())
        if dim_match:
            width, height = map(int, dim_match.groups())

            # Alternative solution from Torchvision repo
            # w, h = (int(dim) for dim in dim_match.groups())
        else:
            raise Exception('Malformed PFM header.')

        scale = float(file.readline().rstrip())

        if scale < 0:  # little-endian
            endian = '<'
            scale = -scale
        else:
            endian = '>'  # big-endian

        data = np.fromfile(file, endian + 'f')
        shape = (height, width, 3) if color else (height, width, 1)

        data = np.reshape(data, shape)
        data = np.flipud(data)
        data = data[:, :, :2]

        # Alternative (adapted from torchvision repo)
        # data = data.reshape(shape).transpose(2, 0, 1)
        # data = np.flip(data, axis=1)  # flip on h dimension
        #data = data[:2, :, :]
        
        data = data.astype(np.float32)

        if self.verbose == 1 :
            t1 = time.time()
            print("Loading time PFM file : " + str(t1-t0) )

        return data

    def write_from_array(self, filepath, np_array, scale=1):
        """
        Write PFM files
        Adapted from : https://github.com/liruoteng/OpticalFlowToolkit
        MIT Licence
        """
        if self.verbose == 1 :
            t0 = time.time()
        file = open(filepath, 'w')

        color = None

        if np_array.dtype.name != 'float32':
            raise Exception('Image dtype must be float32.')

        np_array = np.flipud(np_array)

        array_shape = np_array.shape
        if len(array_shape) == 3 and array_shape[2] == 3:  # color image
            color = True
        elif len(array_shape) == 3 and array_shape[2] == 2:  # 2 channels array, add a third channel
            zero_channel = np.zeros((array_shape[0], array_shape[1], 3), dtype=np.float32)
            zero_channel[:, :, :2] = np_array
            np_array = zero_channel
            color = True
        elif len(array_shape) == 2 or len(array_shape) == 3 and array_shape[2] == 1:  # greyscale
            color = False
        else:
            raise Exception('Image must have H x W x 3, H x W x 1 or H x W dimensions.')

        endian = np_array.dtype.byteorder

        if endian == '<' or endian == '=' and sys.byteorder == 'little':
            scale = -scale

        file.write('PF\n' if color else 'Pf\n')
        file.write('%d %d\n' % (array_shape[1], array_shape[0]))        
        file.write('%f\n' % scale)

        np_array.tofile(file)

        if self.verbose == 1 :
            t1 = time.time()
            print("Writing time PFM file : " + str(t1-t0) )