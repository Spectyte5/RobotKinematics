from visualizer import *

def calculate_fk(theta1_num,theta3_num,theta4_num,d2_num,d5_num,a2_num,a3_num):
    
    # Initialize printing
    sp.init_printing()

    # Define symbolic variables
    theta1 = sp.symbols("theta_1")
    theta3 = sp.symbols("theta_3")
    theta4 = sp.symbols("theta_4")
    d2 = sp.symbols("d_2")
    d5 = sp.symbols("d_5")
    a2 = sp.symbols("a_2")
    a3 = sp.symbols("a_3")

    #A1
    zrot1 = sp.Matrix([[sp.cos(theta1), -sp.sin(theta1), 0, 0],
                       [sp.sin(theta1),  sp.cos(theta1), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

    A1 = zrot1

    # A2
    ztrans2 = sp.Matrix([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, d2],
                        [0, 0, 0, 1]])

    xtrans2 = sp.Matrix([[1, 0, 0, a2],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

    xrot2 = sp.Matrix([[1, 0, 0, 0],
                       [0, sp.cos(sp.rad(-90)), -sp.sin(sp.rad(-90)), 0],
                       [0, sp.sin(sp.rad(-90)), sp.cos(sp.rad(-90)), 0],
                       [0, 0, 0, 1]])

    A2 = ztrans2 * xtrans2 * xrot2

    # A3
    zrot3 = sp.Matrix([[sp.cos(theta3), -sp.sin(theta3), 0, 0],
                       [sp.sin(theta3),  sp.cos(theta3), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

    xtrans3 = sp.Matrix([[1, 0, 0, a3],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])

    A3 = zrot3 * xtrans3

    # A4
    zrot4 = sp.Matrix([[sp.cos(theta4), -sp.sin(theta4), 0, 0],
                    [sp.sin(theta4),  sp.cos(theta4), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    xrot4 = sp.Matrix([[1, 0, 0, 0],
                       [0, sp.cos(sp.rad(90)), -sp.sin(sp.rad(90)), 0],
                       [0, sp.sin(sp.rad(90)), sp.cos(sp.rad(90)), 0],
                       [0, 0, 0, 1]])

    A4 = zrot4 * xrot4

    # A5
    ztrans5 = sp.Matrix([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, d5],
                        [0, 0, 0, 1]])

    A5 = ztrans5

    # Create links
    Link1_sym = A1
    Link2_sym  = A1 * A2
    Link3_sym  = A1 * A2 * A3
    Link4_sym  = A1 * A2 * A3 * A4 
    #TODO: FIX THIS LINK CAUSE ORDER IS WRONG
    Link5_sym  = A1 * A2 * A3 * A4 * A5

    # Substitution 
    Link1=Link1_sym.subs([(theta1, theta1_num)])
    Link2=Link2_sym.subs([(theta1, theta1_num),(a2, a2_num),(d2, d2_num)]) 
    Link3=Link3_sym.subs([(theta1, theta1_num),(a2, a2_num),(d2, d2_num),(theta3, theta3_num), (a3, a3_num)]) 
    Link4=Link4_sym.subs([(theta1, theta1_num),(a2, a2_num),(d2, d2_num),(theta3, theta3_num), (a3, a3_num),(theta4, theta4_num)]) 
    Link5=Link5_sym.subs([(theta1, theta1_num),(a2, a2_num),(d2, d2_num),(theta3, theta3_num), (a3, a3_num),(theta4, theta4_num),(d5, d5_num)]) 

    # Save into array
    Links = [Link1,Link2,Link3,Link4,Link5]

    # Print links
    for l in Links:
        print("\n")
        sp.pprint(l)

    # Draw 3D plot
    draw_fk(Links)


