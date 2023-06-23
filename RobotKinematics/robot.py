from kinematics import *

class Robot:

    def __init__(self,links,dof):
        self.links = links
        self.dof = dof
        self.fkresult = []

    def __str__(self):
        result = f"Robot with:\n DOF:{self.dof}\n"
        result += "\n Links:"
        for l in self.links:
            result += str(l)
        return result

class Link:

    def __init__(self,theta, d, a, alpha, index):
        self.theta = theta
        self.d = d
        self.a = a
        self.alpha = alpha
        self.symbols = ["","","",""]
        if theta != 0:
            self.symbols[0]="theta_" + "%s" %index
        if d != 0:
            self.symbols[1]="d_" + "%s" %index
        if a != 0:
            self.symbols[2]="a_" + "%s" %index
        if alpha != 0:
            self.symbols[3]="alpha_" + "%s" %index

    def __str__(self):
        return f"\n  Link with Symbols:{self.symbols} and Values:[{self.theta},{self.d},{self.a},{self.alpha}]"

