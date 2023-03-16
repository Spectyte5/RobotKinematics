from display import *

def calculate_fk(links):
    
    # Initialize printing
    sp.init_printing()
    
    # Arrays for matrixes
    AMatrixes=[]
    ANum = []
    AFin = []
    A = 1

    for l in links:
        AMatrixes.append(calculateA(l))

    # Substitute
    for i in range(0,len(AMatrixes)-1):
        ANum.append(AMatrixes[i].subs([(links[i].symbols[0],links[i].theta), (links[i].symbols[1],links[i].d),
        (links[i].symbols[2],links[i].a),(links[i].symbols[3], links[i].alpha)]))

    # Calculate link matrixes
    for An in ANum:
        A *= An
        AFin.append(A)


    # Additional link for geometry
    #LinkA = sp.Matrix  ([[0, 0, 0, 0],
     #                   [0, 0, 0, 0],
      #                  [0, 0, 0, 700],
       #                 [0, 0, 0, 0]])
    
    # Save into array <- change name to sth else
    #Links = [Link1,LinkA,Link2,Link3,Link4,Link5] 
    #Del = []
    
    # Remove links with the same position cordinates from plotting
    #for i in range(1,len(Links)):
     #   if Links[i][0,3] == Links[i-1][0,3] and Links[i][1,3] == Links[i-1][1,3] and Links[i][2,3] == Links[i-1][2,3]:
      #      Del.append(i)
    #for d in Del:
     #   Links.remove(Links[d])

    # Draw 3D plot
    draw_fk(links, AFin)

    # Matrixes for IK
    #T03 = A1*A2*A3
    #Te = A4*A5
    #p3a = sp.Matrix([0,0,0,1])
    #T03v=T03.subs([(theta1, 'q_1'),(theta3, 'q_3')])
    #Tev=Te.subs([(theta4, 'q_1'),(theta3, 'q_3')])
    #Ik_matrixes = [T03v,Tev,p3a]

    #return Ik_matrixes
    

def calculate_ik(Ik_matrixes):
   
    # marixes from FK
    d5 = sp.symbols("d_5")
    T03 = Ik_matrixes[0]
    Te = Ik_matrixes[1]
    p3a = Ik_matrixes[2]

    # position calculation
    P = sp.Matrix([Te[0,3],Te[1,3],Te[2,3]])
    Pw = d5 * sp.Matrix([Te[0,2],Te[1,2],Te[2,2]])
    Pa = P - Pw
    sp.pprint(P)
    sp.pprint(Pw)

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

    rz = sp.Matrix([[sp.cos(theta), -sp.sin(theta), 0, 0],
                    [sp.sin(theta),  sp.cos(theta), 0, 0],
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
