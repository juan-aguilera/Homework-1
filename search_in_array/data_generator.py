import random
from array import array
import constants


def random_list(size, lim = constants.MAX_VALUE):
    ran_list =[]
    while len(ran_list) < size : 
        ran_list.append(random.randint(0, lim))
    ran_list.sort()
    ran_array =array('i',ran_list)   
    return ran_array

def gen_target(sample_array):
    return random.choice(sample_array)