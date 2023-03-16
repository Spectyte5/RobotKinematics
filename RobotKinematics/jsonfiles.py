import json
from Link import *

def load_json(): 
    with open('./Json/lab.json') as user_file:
        ufile = user_file.read()
    parsed_json = json.loads(ufile)
    
    json_links=parsed_json["Links"]
    Links = []
    Symbols = []
   
    for link in json_links:
        L=Link(link[0],link[1],link[2],link[3], json_links.index(link)+1)
        Links.append(L)
        print(L)

    return Links

def checkifzero(iter) :
    for item in iter :
        if item != 0 :
            return iter.index(item)