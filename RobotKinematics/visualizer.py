import math
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_fk(Links):

    # create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # link cordinates
    xq = (Links[0][0,3], Links[1][0,3], Links[2][0,3], Links[3][0,3])
    yq = (Links[0][1,3], Links[1][1,3], Links[2][1,3], Links[3][1,3])
    zq = (Links[0][2,3], Links[1][2,3], Links[2][2,3], Links[3][2,3])
    uq = (Links[1][0,3], Links[2][0,3], Links[3][0,3], Links[4][0,3])
    vq = (Links[1][1,3], Links[2][1,3], Links[3][1,3], Links[4][1,3])
    wq = (Links[1][2,3], Links[2][2,3], Links[3][2,3], Links[4][2,3])

    for x, y, z, u, v, w in zip(xq, yq, zq, uq, vq, wq):
        ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0)

    # joints cordinates
    xs = (Links[0][0,3], Links[1][0,3], Links[2][0,3], Links[3][0,3], Links[4][0,3])
    ys = (Links[0][1,3], Links[1][1,3], Links[2][1,3], Links[3][1,3], Links[4][1,3])
    zs = (Links[0][2,3], Links[1][2,3], Links[2][2,3], Links[3][2,3], Links[4][2,3])

    for x, y, z in zip(xs, ys, zs):
        ax.scatter(x,y,z,color='k')
        label = '(%d, %d, %d)' % (x, y, z)
        ax.text(x, y, z, label)

    # set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # display plot
    plt.show()
