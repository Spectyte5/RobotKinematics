from email.utils import decode_rfc2231
import math
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_fk(Links):

    # initial degrees of fredom
    dof = 0

    # create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # empty turples for cordinates
    xs = ys = zs = ()
    xq = yq = zq = uq = vq = wq = ()
 
    # joints cordinates
    for L in Links:
        xs += (L[0,3],)
        ys += (L[1,3],)
        zs += (L[2,3],)  

    # link cordinates
    for i in range(1,len(Links)):
        # inital point of the vector
        xq += (Links[i-1][0,3],)
        yq += (Links[i-1][1,3],)
        zq += (Links[i-1][2,3],) 
        # calculate change of position
        xdir = Links[i][0,3]-Links[i-1][0,3]
        ydir = Links[i][1,3]-Links[i-1][1,3]
        zdir = Links[i][2,3]-Links[i-1][2,3]
        # direction of the vector
        uq += (xdir,)
        vq += (ydir,)
        wq += (zdir,)  

    # plot joints
    for x, y, z in zip(xs, ys, zs):
        if dof == 0:
            ax.scatter(x,y,z,s=100,marker="s",color='k')
        elif dof == len(Links)-1:
            ax.scatter(x,y,z,s=50,marker="s",color='k')
            dof -= 1
        else:
            ax.scatter(x,y,z,s=50,color='k')
        label = '(%d, %d, %d)' % (x, y, z)
        ax.text(x, y, z, label)
        dof += 1
    
    # plot links
    for x, y, z, u, v, w in zip(xq, yq, zq, uq, vq, wq):
        ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0)

    # set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # display plot
    plt.suptitle("Forward Kinematics of the Robotic arm with %s DOF" %dof)
    plt.savefig('./Plots/Robot_FK.png')
    plt.show()
    
