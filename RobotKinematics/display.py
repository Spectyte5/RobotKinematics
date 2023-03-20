import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_fk(robot, AFin):

    # create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # empty turples for cordinates
    xs = ys = zs = ()
    xq = yq = zq = uq = vq = wq = ()
 
    # joints cordinates
    for A in AFin:
        xs += (A[0,3],)
        ys += (A[1,3],)
        zs += (A[2,3],)  

    # link cordinates
    for i in range(1,len(AFin)):
        # inital point of the vector
        xq += (AFin[i-1][0,3],)
        yq += (AFin[i-1][1,3],)
        zq += (AFin[i-1][2,3],) 
        # calculate change of position
        xdir = AFin[i][0,3]-AFin[i-1][0,3]
        ydir = AFin[i][1,3]-AFin[i-1][1,3]
        zdir = AFin[i][2,3]-AFin[i-1][2,3]
        # direction of the vector
        uq += (xdir,)
        vq += (ydir,)
        wq += (zdir,)  

    # plot joints
    for x, y, z in zip(xs, ys, zs):
        ax.scatter(x,y,z,s=50,color='k')
        label = '(%d, %d, %d)' % (x, y, z)
        ax.text(x, y, z, label)

    # plot links
    for x, y, z, u, v, w in zip(xq, yq, zq, uq, vq, wq):
        ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0)

    # set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # display plot
    plt.suptitle("Forward Kinematics of the Robotic arm with %s DOF" %robot.dof)
    plt.savefig('./Plots/Robot_FK.png')
    plt.show()
    
