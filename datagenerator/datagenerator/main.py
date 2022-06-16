import os
import sys
import numpy as np
import bpy
import time
import datetime

from datagenerator.utils.arguments import *
from datagenerator.trajectories.keyframes import *
from datagenerator.trajectories.types import *
from datagenerator.trajectories.load import *

def main(argv):
    print("Initializing data generation")
    print("Arguments given : ")
    print(argv)  # --> ['example', 'args', '123']
    print("\n")

    t0 = time.time()


    scene, trajectory_filepath, initial_translation, initial_rotation = check_input_arguments(argv)
    print(check_input_arguments(argv))

    #
    # Read scene
    #
    bpy.ops.wm.open_mainfile(filepath=scene)
    objects = []

    cameras_frame = bpy.data.objects['CamerasFrame']
    objects.append(cameras_frame)

    #
    # Load trajectory
    #
    context = bpy.context
    for ob in context.selected_objects:
        ob.animation_data_clear() # Clear any existing keypoint
    #bpy.context.active_object.animation_data_clear() # Clear any existing keypoint
    trajectory_type = guess_trajectory_type(trajectory_filepath)
    trajectory, num_frames = load_trajectory(trajectory_type, trajectory_filepath)
    modified_trajectory = modify_trajectory(trajectory, initial_translation, initial_rotation)
    insert_keyframes(modified_trajectory, cameras_frame)

    #
    # Process trajectory
    #

    print("proccessing image")

    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_current = 0

    for i in range(num_frames):
        t_init_frame = time.time()
        bpy.ops.render.render(write_still = False)
        bpy.ops.screen.keyframe_jump()
        t_end_frame = time.time()
        print("PROCESSING TIME FRAME : ", t_end_frame - t_init_frame)

    t1 = time.time()

    print("TOTAL DURATION : %s" %str(t1-t0))
    #print(datetime.utcfromtimestamp(t1).strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]  # get all args after "--"
    main(argv)
