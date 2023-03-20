from kinematics import *
from jsonfiles import *

# load data from the file
robot=load_json()
# calculate forward and inverse kinematics
if robot.fk:
    calculate_fk(robot)
if robot.ik:
    calculate_ik(robot)