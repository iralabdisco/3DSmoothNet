# 3DSmoothNet 

1. Generate the Smoothed Density Valie (SVD) voxel grid and keypoints (saved as .pcd) using the `voxelize_all.py`. Modify the input and output direcotries at the beginning of hte file. The parameters for the SVD grid are stored in the `voxel_parameters.yaml` file. Do not modify the directory parameters in the .yaml file, they are update autmatically by the script.
2. Use the `run_benchmark_global.py` to generate the features from the SVD rapresentation.
3. Use the `join_all.py` script to merge keypoints and features in a single .npz file.
