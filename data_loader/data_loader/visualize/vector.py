import numpy as np
import oflibnumpy

class MotionFlowVisualizer(object):

    def __init__(self) -> None:
        self.motion_flow_array = None

    def load(self, flow_array : np.array) -> None:
        self.motion_flow_array = flow_array

    def visualize_arrows(self, density : int) -> np.array:
        motion_flow = oflibnumpy.Flow(self.motion_flow_array)
        return motion_flow.visualise_arrows(density, colour=(0, 0, 0))

    def visualize_coloured_arrows(self, density : int) -> np.array:
        motion_flow = oflibnumpy.Flow(self.motion_flow_array)
        return motion_flow.visualise_arrows(density)

    def visualize_dense_coloured(self) -> np.array:
        motion_flow = oflibnumpy.Flow(self.motion_flow_array)
        return motion_flow.visualise('bgr')

    def get_definition_dense_coloured(self)->np.array:
        return oflibnumpy.visualise_definition('bgr')