import os, shutil
from multiprocessing import Pool
from pathlib import Path

PY3="python3"

GPU = "0"
os.environ["CUDA_VISIBLE_DEVICES"] = GPU

FEATURES_DIR="/benchmark/experiments/3DSmoothNet/features/"
OUTPUT_DIM = "64"

base_command = ( "python3 main_cnn.py --run_mode=test --output_dim="+OUTPUT_DIM + " ")

problem_txts = ['kaist/urban05_global.txt',
                'eth/apartment_global.txt',
                'eth/gazebo_summer_global.txt',
                'eth/gazebo_winter_global.txt',
                'eth/hauptgebaude_global.txt',
                'eth/plain_global.txt',
                'eth/stairs_global.txt',
                'eth/wood_autumn_global.txt',
                'eth/wood_summer_global.txt',
                'tum/long_office_household_global.txt',
                'tum/pioneer_slam_global.txt',
                'tum/pioneer_slam3_global.txt',
                'planetary/box_met_global.txt',
                'planetary/p2at_met_global.txt',
                'planetary/planetary_map_global.txt']

pcd_dirs = ['kaist/urban05/',
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
            'planetary/p2at_met/',
            'planetary/p2at_met/']

commands = []

for problem_txt, pcd_dir in zip(problem_txts, pcd_dirs):
    full_command = (base_command +
                    "--evaluate_input_folder " + FEATURES_DIR+"/"+pcd_dir +
                    " --evaluate_output_folder=" + FEATURES_DIR+"/"+pcd_dir)

    problem_name = Path(problem_txt).stem
    time_command = "'command time --verbose -o "+ FEATURES_DIR+"/"+problem_name+"_cnn_time.txt " + full_command + "'"
    nvidia_command = " 'nvidia-smi --query-gpu=timestamp,memory.used -i 0 --format=csv -lms 1 > "+FEATURES_DIR+"/"+problem_name+"_cnn_memory.txt'"

    full_command_stats = "parallel -j2 --halt now,success=1 ::: " + time_command + nvidia_command
    commands.append(full_command_stats)

for command in commands:
    print(command)
    os.system(command)

# save config in result directory
txt_commands = os.path.join(FEATURES_DIR, "readme_cnn.md")
with open(txt_commands, 'w') as f:
    for item in commands:
        f.write("%s\n" % item)

# pool = Pool(1)
# pool.map(os.system, commands)