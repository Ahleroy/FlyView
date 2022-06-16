import bpy
import random
import os
from scipy.spatial.transform import Rotation
from mathutils import Quaternion

def insert_keyframes(trajectory, object):
        object.rotation_mode = 'QUATERNION'
        for id_keyframe, row in trajectory.iterrows():
            x = row["X"]
            y = row["Y"]
            z = row["Z"]
            qw = row["Qw"]
            qx = row["Qx"]
            qy = row["Qy"]
            qz = row["Qz"]
            q = Quaternion([qw, qx, qy, qz])
            object.location = (x, y, z)
            object.rotation_quaternion = q
            object.keyframe_insert(data_path="location", frame=id_keyframe)
            object.keyframe_insert(data_path="rotation_quaternion", frame=id_keyframe)
            