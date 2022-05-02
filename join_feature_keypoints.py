import numpy, argparse, open3d, pathlib, os, glob

parser = argparse.ArgumentParser(description='Join keypoints and 3DSmoothNet features in a single file')
# parser.add_argument('--keypoints', '-k', type=str, required = True)
parser.add_argument('--folder', '-f', type=str, required = True)  
parser.add_argument('--out_folder', '-o', type=str, required = True)  
args = parser.parse_args()

files = glob.glob(args.folder+'/*_3DSmoothNet.npz')

for file in files:
    print(file)
    features = numpy.load(file)['data']
    folder = os.path.dirname(file)
    save_name = pathlib.Path(file).stem
    save_name = save_name.replace("_3DSmoothNet",'')
    keypoints = open3d.io.read_point_cloud(os.path.join(folder,save_name+'_keypoints.pcd'))
    keypoints = numpy.asarray(keypoints.points)

    save_name = os.path.join(args.out_folder, save_name+".npz")

    numpy.savez_compressed(save_name, xyz_down=keypoints, features=features)