#!/usr/bin/env python
# -*- coding: future_fstrings -*-

import os
import argparse
import logging

import shutil
import numpy as np
from tqdm import tqdm
import pandas as pd
import open3d as o3d
from pathlib import Path
import yaml
from types import SimpleNamespace    

import benchmark_helper

def main():
    parser = argparse.ArgumentParser(description='3DSmoothNet Voxelization')
    parser.add_argument('parameters', type=str, help='Path to the yaml parameters file')  
    args = parser.parse_args()
    
    with open(args.parameters,'r') as file:
        parameter = yaml.load(file, Loader=yaml.FullLoader)
    print(parameter)
    params = SimpleNamespace(**parameter)

    os.makedirs(params.output_dir, exist_ok=True)
    shutil.copyfile(args.parameters, f"{params.output_dir}/{args.parameters}")

    ## Load problems txt file
    df = pd.read_csv(params.problem_file, sep=' ', comment='#')
    df = df.reset_index()
    n_problems = len(df.index)

    voxelization_parameters =  f"""-k {params.frac_points} -r {params.voxel_size} -n {params.vox_num} -h {params.gauss_width} -o {params.output_dir}"""

    num_processed = 0
    ## Solve for each problem
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        problem_id, source_pcd, target_pcd, source_transform, target_pcd_filename = \
                         benchmark_helper.load_problem(row, params)

        ## Extract features from source
        source_base_name = os.path.join(params.output_dir, '{}'.format(problem_id))
        source_pcd.transform(source_transform)
        o3d.io.write_point_cloud(f"{source_base_name}.pcd", source_pcd)
        os.system(f"/home/3DSmoothNet/3DSmoothNet -f {source_base_name}.pcd {voxelization_parameters}")
        os.system(f"rm {source_base_name}.pcd")

        ## Extract features from target
        target_file_name = os.path.join(params.input_pcd_dir, target_pcd_filename)
        target_out_name = os.path.join(params.output_dir, target_pcd_filename)
        if not(os.path.isfile(f"{Path(target_out_name).stem}.csv")):   
            os.system(f"/home/3DSmoothNet/3DSmoothNet -f {target_file_name} {voxelization_parameters}")
        
if __name__ == '__main__':
    main()