import os
import numpy as np

def check_float(value):
    try:
        if value is not None:
            fvalue = float(value)
        else:
            fvalue = None
    except ValueError:
        fvalue = None

    return fvalue

def check_str(value):
    return isinstance(value, str)

def check_path(value):
    if not isinstance(value, str):
        exit("Not a string")

    filename = os.path.isfile(path)
    
def check_input_arguments(argv):

    if len(argv) not in [2, 5, 6, 9]:
        print("Please make sure the correct number of parameters are given")

    
    # arg 1 : scene
    #scene_filepath = check_str(argv[0])
    scene_filepath = argv[0]

    # arg 2 : trajectory filepath
    #trajectory_filepath = check_str(argv[1])
    trajectory_filepath = argv[1]

    # arg 3 : X translation offset
    X = check_float(argv[2])

    # arg 4 : Y translation offset
    Y = check_float(argv[3])
    # arg 5 : Z translation offset
    Z = check_float(argv[4])
    # arg 6 : ZRot in degrees
    ZRot = check_float(argv[5])
    # arg 7 : Qw rotation offset
    # Qx = check_float(argv[6])
    # # arg 8 : Qw rotation offset
    # Qy = check_float(argv[7])
    # # arg 9 : Qw rotation offset
    # Qz = check_float(argv[8])

    translation = np.array([X, Y, Z], dtype=np.float64)
    #rotation = np.array([Qw, Qx, Qy, Qz], dtype=np.float64)

    return scene_filepath, trajectory_filepath, translation, ZRot