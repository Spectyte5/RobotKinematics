from kinematics import *
from jsonfiles import *

links=load_json()
#fk_result=calculate_fk(fk_variables)
calculate_fk(links)
#calculate_ik(fk_result)