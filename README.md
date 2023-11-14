# 3DSmoothNet 

1. Generate the Smoothed Density Valie (SVD) voxel grid and keypoints (saved as .pcd) using the `voxelize_all.py`. Modify the input and output direcotries at the beginning of hte file. The parameters for the SVD grid are stored in the `voxel_parameters.yaml` file. Do not modify the directory parameters in the .yaml file, they are update autmatically by the script.
2. Use the `run_benchmark_global.py` to generate the features from the SVD rapresentation.
3. Use the `join_all.py` script to merge keypoints and features in a single .npz file.

## SLAM example

1. `voxelize_tum_slam.py`
2. `run_benchmark_global.py` (modify the )
3. `join_feature_keypoints.py --cnn_dim 64 -f /benchmark/tum_slam_comparison/3DSmoothNet/features/pioneer_slam2_025/ -o /benchmark/tum_slam_comparison/3DSmoothNet/features/pioneer_slam2_025/`