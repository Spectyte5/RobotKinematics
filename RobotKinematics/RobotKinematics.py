from re import X
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
sp.init_printing()

# Define symbolic variables
theta1 = sp.symbols("theta_1")
theta3 = sp.symbols("theta_3")
theta4 = sp.symbols("theta_4")
d2 = sp.symbols("d_2")
d5 = sp.symbols("d_5")
a2 = sp.symbols("d_2")
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

xtrans3 = sp.Matrix([[1, 0, 0, a2],
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

# Final matrix
Result = A1 * A2 * A3 * A4 * A5


# Graphical solution
th1 = 0
th3 = 0
th4 = 0
d_2 = 100
d_5 = 100
a_2 = 100
a_3 = 100

X=np.array([[]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0,0,0,s=100,color='k') 
ax.quiver(0,0,0,0,0,d_2,arrow_length_ratio=0)
ax.scatter(0,0,d_2,color='k') 
ax.quiver(0,0,d_2,a_2,0,0,arrow_length_ratio=0)
ax.scatter(a_2,0,d_2,color='k') 
ax.quiver(a_2,0,d_2,a_3,0,0,arrow_length_ratio=0)
ax.scatter(a_2+a_3,0,d_2,color='k') 
ax.quiver(a_2+a_3,0,d_2,0,0,d_5,arrow_length_ratio=0)
ax.scatter(a_2+a_3,0,d_2+d_5,color='k') 
ax.set_xlim([-400, 400])
ax.set_ylim([-400, 400])
ax.set_zlim([0, 200])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()