import os
from pathlib import Path

PY3="python3"

GPU = "0"
os.environ["CUDA_VISIBLE_DEVICES"] = GPU

FEATURES_DIR="/benchmark/experiments/3DSmoothNet/features/"
OUTPUT_DIM = "64"

base_command = ("python3 join_feature_keypoints.py --cnn_dim="+OUTPUT_DIM)

features_dirs = ['kaist/urban05/',
            'eth/apartment/',
            'eth/gazebo_summer/',
            'eth/gazebo_winter/',
            'eth/hauptgebaude/',
            'eth/plain/',
            'eth/stairs/',
            'eth/wood_autumn/',
            'eth/wood_summer/',
            'tum/long_office_household/',
            'tum/pioneer_slam/',
            'tum/pioneer_slam3/',
            'planetary/box_met/',
            'planetary/p2at_met/']

commands = []

for features_dir in features_dirs:
    full_command = (base_command +
                    " -f " + FEATURES_DIR+"/"+features_dir +
                    " -o " + FEATURES_DIR+"/"+features_dir)
    commands.append(full_command)

for command in commands:
    print(command)
    os.system(command)