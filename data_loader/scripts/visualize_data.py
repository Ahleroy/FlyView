from matplotlib.image import imsave
from data_loader.utils.exr import EXRFile
from data_loader.visualize.vector import MotionFlowVisualizer

import cv2
import os
import sys
import glob
import numpy as np


file_corridor = "/<path_to_file>/0001_FishEye_Center_EquiRect.exr"

# List of channels we want to extract from the EXR file [depth, forward_flow, backward_flow]
channels = [("Depth_.V",), ("NegForwardX_.V", "NegForwardY_.V",), ("BackwardX_.V", "BackwardY_.V",)]

# Key names of the output dictionary
channels_name_output = ["depth", "negforward_flow", "backward_flow"]

# Initialize an EXR file
exr_file = EXRFile(verbose = 1)

# Open the EXR file
output_file = exr_file.open(file_corridor, channels, channels_name_output)

# Get the outputs
depth = output_file["depth"]
flow = output_file["negforward_flow"]
back_flow = output_file["backward_flow"]

# Process depth map for visualization
depth_map_visualize = np.where(depth > 100, 100, depth)
depth_map_visualize = np.log1p(depth_map_visualize)
depthmap_grayscale = cv2.normalize(depth_map_visualize,None,0,255,cv2.NORM_MINMAX)
depthmap_grayscale = np.array(depthmap_grayscale, dtype=np.uint8)
depthmap_colored = cv2.applyColorMap(depthmap_grayscale, cv2.COLORMAP_JET)


# Process motion flow for visialization
THRESHOLD_FLOW = 2
flow = np.where(flow > THRESHOLD_FLOW, THRESHOLD_FLOW, flow)
flow = np.where(flow < -THRESHOLD_FLOW, -THRESHOLD_FLOW, flow)

# Orient the X axis correctly
flow[:, :, 0] = -flow[:, :, 0]

visualizer = MotionFlowVisualizer()
visualizer.load(flow)
bgr_img = visualizer.visualize_dense_coloured()
arrow_img = visualizer.visualize_arrows(50)

# Save the viualizations
cv2.imwrite("depth_map.png", depthmap_colored)
cv2.imwrite("flow_coloured.png", bgr_img)
cv2.imwrite("flow_arrow.png", arrow_img)