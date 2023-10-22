#!/usr/bin/env python
# -*- coding: future_fstrings -*-

import glob, sys, os, yaml
from multiprocessing import Pool

benchmark_folder = "/SSD/neural_comparison/point_clouds_registration_benchmark/datasets_outlier_removal_mean10_dev3_voxelgrid_0.05"
executable = "python /home/3DSmoothNet/exec_on_benchmark.py"
problem_folder = f'/SSD/neural_comparison/point_clouds_registration_benchmark/devel/registration_pairs'
output_dir =  "/SSD/neural_comparison/features/3DSmoothNet/"
parameter_file = "voxel_parameters.yaml"

subfolders = ["eth/apartment/", "eth/stairs/","eth/plain/","eth/hauptgebaude/", "eth/gazebo_summer/", "eth/gazebo_winter/",
    "eth/wood_summer/", "eth/wood_autumn/", "planetary/p2at_met/", "planetary/box_met/", "planetary/p2at_met/", 
    "tum/long_office_household/",  "tum/pioneer_slam/", "tum/pioneer_slam3/", "kaist/urban05/"]

problem_files = ["apartment_global.txt", "stairs_global.txt", "plain_global.txt", "hauptgebaude_global.txt", 
    "gazebo_summer_global.txt", "gazebo_winter_global.txt", "wood_summer_global.txt", "wood_autumn_global.txt", 
    "p2at_met_global.txt", "box_met_global.txt ", "planetary_map_global.txt", "long_office_household_global.txt",  
    "pioneer_slam_global.txt", "pioneer_slam3_global.txt", "urban05_global.txt"]

for problem, folder in zip(problem_files, subfolders):
    with open(parameter_file, 'r') as file:
        parameters = yaml.full_load(file)
    parameters['problem_file'] = os.path.join(problem_folder, problem)
    parameters['input_pcd_dir'] = os.path.join(benchmark_folder, folder)
    parameters['output_dir'] = os.path.join(output_dir, folder)

    with open(parameter_file, 'w') as file:
        yaml.dump(parameters, file)

    os.system(f"{executable} {parameter_file}")
