from display import *
import numpy as np

def calculate_fk(robot):
    
    # Initialize printing
    sp.init_printing()
    
    # Arrays for matrixes
    AMatrixes=[]
    ANum = []
    A = 1

    for l in robot.links:
        AMatrixes.append(calculateA(l))

    # Substitute
    for i in range(0,len(AMatrixes)):
        ANum.append(AMatrixes[i].subs([(robot.links[i].symbols[0],robot.links[i].theta), (robot.links[i].symbols[1],robot.links[i].d),
        (robot.links[i].symbols[2],robot.links[i].a),(robot.links[i].symbols[3], robot.links[i].alpha)]))

    # Calculate link matrixes
    for An in ANum:
        A *= An
        robot.fkresult.append(A)
    
    # print fk result
    print('Fk Result:')
    sp.pprint(robot.fkresult[-1])
    
    # return for tests
    return robot.fkresult[-1]

def calculateA(link):

    A1=rotz(link.symbols[0])
    A2=traz(link.symbols[1])
    A3=trax(link.symbols[2])
    A4=rotx(link.symbols[3])
    return A1*A2*A3*A4

def rotz(theta_val):

    if not theta_val:
        theta = 0
    else:
        theta = sp.symbols(theta_val)

    rz = sp.Matrix([[sp.cos(sp.rad(theta)), -sp.sin(sp.rad(theta)), 0, 0],
                    [sp.sin(sp.rad(theta)),  sp.cos(sp.rad(theta)), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return rz

def traz(d_val):

    if not d_val:
        d = 0
    else:
        d = sp.symbols(d_val)

    tz = sp.Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, d],
                    [0, 0, 0, 1]])
    return tz

def trax(a_val):
    
    if not a_val:
        a = 0
    else:
        a = sp.symbols(a_val)

    tx = sp.Matrix([[1, 0, 0, a],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return tx

def rotx(alpha_val):

    if not alpha_val:
        alpha = 0
    else:
        alpha = sp.symbols(alpha_val)

    rx = sp.Matrix([[1, 0, 0, 0],
                    [0, sp.cos(sp.rad(alpha)), -sp.sin(sp.rad(alpha)), 0],
                    [0, sp.sin(sp.rad(alpha)), sp.cos(sp.rad(alpha)), 0],
                    [0, 0, 0, 1]])
    return rx
