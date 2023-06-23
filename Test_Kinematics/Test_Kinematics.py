import numpy as np
import pytest
import sys
sys.path.insert(0, '../RobotKinematics')
from kinematics import *

# Class for testing kinematics
class TestKinematics:
    # Test inverse kinematics
    @pytest.mark.parametrize("dh_table, end_effector_pose, expected_joint_angles", [
        # Test Case 1
        ([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], np.eye(4), [0, 0, 0, 0, 0, 0, 0]),

        # Test Case 2
        ([
            [0, 100, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], np.eye(4), [0, 100, 0, 0, 0, 0, 0]),

        # Add more test cases as needed
    ])
    def test_inverse_kinematics(self, dh_table, end_effector_pose, expected_joint_angles):
        # Call the inverse kinematics function
        calculated_joint_angles = calculate_inverse_kinematics(dh_table, end_effector_pose)

        # Check if the calculated joint angles match the expected joint angles
        assert np.allclose(calculated_joint_angles, expected_joint_angles)

    # Test forward kinematics
    @pytest.mark.parametrize("dh_table, joint_angles, expected_end_effector_pose", [
        # Test Case 1
        ([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], [0, 0, 0, 0, 0, 0, 0], np.eye(4)),

        # Test Case 2
        ([
            [0, 100, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], [0, 100, 0, 0, 0, 0, 0], np.eye(4)),

        # Add more test cases as needed
    ])
    def test_forward_kinematics(self, dh_table, joint_angles, expected_end_effector_pose):
        # Call the forward kinematics function
        calculated_end_effector_pose = calculate_forward_kinematics(dh_table, joint_angles)
        assert np.allclose( calculated_end_effector_pose, expected_end_effector_pose)
