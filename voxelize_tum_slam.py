#!/usr/bin/env python
# -*- coding: future_fstrings -*-

import os, yaml
from pathlib import Path

benchmark_folder = "/benchmark/tum_slam_comparison/"
executable = "python /home/docker/3DSmoothNet/exec_on_benchmark.py"
problem_folder = "/benchmark/tum_slam_comparison/"
output_dir = "/benchmark/tum_slam_comparison/3DSmoothNet/features/"
parameter_file = "voxel_parameters.yaml"

subfolders = ["pioneer_slam2_025/"]

problem_files = ["pioneer_slam2_problems.txt"]

for problem, folder in zip(problem_files, subfolders):
    with open(parameter_file, 'r') as file:
        parameters = yaml.full_load(file)
    parameters['problem_file'] = os.path.join(problem_folder, problem)
    parameters['input_pcd_dir'] = os.path.join(benchmark_folder, folder)
    parameters['output_dir'] = os.path.join(output_dir, folder)

    with open(parameter_file, 'w') as file:
        yaml.dump(parameters, file)

    print(os.path.join(output_dir, folder))
    print(parameters)

    base_command = executable + " " + parameter_file
    problem_name = Path(problem).stem
    time_command = "command time -v -o " + output_dir + "/" + problem_name + "_voxelization_time.txt " + base_command
    print(time_command)
    os.system(time_command)
