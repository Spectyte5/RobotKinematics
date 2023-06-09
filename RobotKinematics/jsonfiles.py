import json
from robot import *

def load_json(): 
    with open('./Json/robot.json') as user_file:
        ufile = user_file.read()
    parsed_json = json.loads(ufile)
    
    #read data
    json_links=parsed_json["Robot"]["Links"]
    dof = parsed_json["Robot"]["DOF"]
    Links = []
   
    for link in json_links:
        L=Link(link[0],link[1],link[2],link[3], json_links.index(link)+1)
        Links.append(L)

    # create robot object
    robot=Robot(Links,dof)
    print(robot)
    return robot

def checkifzero(iter) :
    for item in iter :
        if item != 0 :
            return iter.index(item)