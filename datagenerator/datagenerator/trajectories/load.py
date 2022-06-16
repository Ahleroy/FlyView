import bpy
import pandas as pd
import random
import os
from scipy.spatial.transform import Rotation
from mathutils import Quaternion
import numpy as np

def load_trajectory(type, filepath):
    poses = []
    line = 0
    if type == "bird_flight":

        with open(filepath, "r") as f:
            lines = f.readlines()
        
        for idx_line, l in enumerate(lines):
            id_keyframe = idx_line - 2
            if idx_line == 0:
                continue
            elif idx_line == 1:
                continue
            else:
                data = l.split(",")
                x = float(data[5])/100 # Bird translation is expressed in cm
                y = float(data[5])/100
                z = float(data[5])/100
                qw = float(data[12])
                qx = float(data[13])
                qy = float(data[14])
                qz = float(data[15])
                pose = [x, y, z, qw, qx, qy, qz]
                poses.append(pose)
    elif type == "computer_generated":

        with open(filepath, "r") as f:
            lines = f.readlines()
        
        for idx_line, l in enumerate(lines):
            id_keyframe = idx_line - 1
            if idx_line == 0:
                continue
            else:
                data = l.split(",")
                x = float(data[0])
                y = float(data[1])
                z = float(data[2])
                qw = float(data[3])
                qx = float(data[4])
                qy = float(data[5])
                qz = float(data[6])

                pose = [x, y, z, qw, qx, qy, qz]
                poses.append(pose)

    elif type == "drone": 

        with open(filepath, "r") as f:
            lines = f.readlines()
        
        for idx_line, l in enumerate(lines):
            id_keyframe = idx_line - 1
            if idx_line == 0:
                continue
            else:
                data = l.split(",")
                # If there is an empty line, skip it
                if data[0] == "":
                    continue
                x = float(data[0]) /1000 # Drone translation is expressed in millimeters
                y = float(data[1]) /1000
                z = float(data[2]) /1000
                qw = float(data[3])
                qx = float(data[4])
                qy = float(data[5])
                qz = float(data[6])

                pose = [x, y, z, qw, qx, qy, qz]
                poses.append(pose)
    df = pd.DataFrame(poses, columns=["X", "Y", "Z", "Qw", "Qx", "Qy", "Qz"])
    return df, len(lines)

def modify_trajectory(trajectory, initial_translation, initial_rotation):
    print(trajectory["Z"])

    # Get very first position of the trajectory
    first_pose_x = trajectory["X"][0]
    first_pose_y = trajectory["Y"][0]
    first_pose_z = trajectory["Z"][0]

    # Offset to origin
    trajectory["X"] = trajectory["X"] - first_pose_x
    trajectory["Y"] = trajectory["Y"] - first_pose_y
    trajectory["Z"] = trajectory["Z"] - first_pose_z

    # Create homogeneous rotation matrx 
    yaw_rotation = Rotation.from_euler("z", initial_rotation, degrees=True)
    mat_rot = yaw_rotation.as_matrix()
    mat_rot_4x4 = np.zeros((4, 4), dtype=np.float64)
    mat_rot_4x4[:-1, :-1] = mat_rot
    mat_rot_4x4[-1, -1] = 1

    for index, row in trajectory.iterrows():
        # Homogeneous coordinates of point
        translation = np.array([row["X"], row["Y"], row["Z"], 1])

        # New translation point
        new_translation = mat_rot_4x4 @ translation

        # Current rotation
        rotation = Rotation.from_quat([row["Qx"], row["Qy"], row["Qz"], row["Qw"]])
        
        # Compute new rotation
        new_rotation = yaw_rotation * rotation
        new_rot_quat = new_rotation.as_quat()
        
        # Change translation
        trajectory.at[index, "X"] = new_translation[0]
        trajectory.at[index,"Y"] = new_translation[1]
        trajectory.at[index,"Z"] = new_translation[2]

        # Change rotation
        trajectory.at[index,"Qw"] = new_rot_quat[3]
        trajectory.at[index,"Qx"] = new_rot_quat[0]
        trajectory.at[index,"Qy"] = new_rot_quat[1]
        trajectory.at[index,"Qz"] = new_rot_quat[2]

    # Remove offset and add potential additional translation given in argument
    trajectory["X"] = trajectory["X"] + first_pose_x + initial_translation[0] 
    trajectory["Y"] = trajectory["Y"] + first_pose_y + initial_translation[1] 
    trajectory["Z"] = trajectory["Z"] + first_pose_z + initial_translation[2] 


    return trajectory
