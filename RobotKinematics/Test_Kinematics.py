import numpy as np
import pytest
import sys
sys.path.insert(0, '../RobotKinematics')
from robot import *

class TestKinematics:
    @pytest.mark.parametrize("dh_table, expected_end_effector_pose", [
        ([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], np.eye(4)),
        ([
            [0, 100, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], 
        np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 100],
                   [0, 0, 0, 1]])
        )])

    def test_forward_kinematics(self, dh_table, expected_end_effector_pose):
        Links = []
        for link in dh_table:
            L=Link(link[0],link[1],link[2],link[3], dh_table.index(link)+1)
            Links.append(L)
        robot = Robot(Links,7)
        calculated_end_effector_pose = np.array(calculate_fk(robot).tolist(), dtype=float)
        assert np.allclose( calculated_end_effector_pose, expected_end_effector_pose)


