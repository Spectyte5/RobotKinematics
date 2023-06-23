from kinematics import *
from jsonfiles import *

# load data from the file
separator = '=' * 100
robot=load_json()
print(separator)
# calculate forward and inverse kinematics
calculate_fk(robot)
print(separator)
# Draw 3D plot
draw_fk(robot)