import random
from search_in_array import constants

def random_list(size, lim = constants.MAX_VALUE):
    ran_list = []
    while len(ran_list) < size : 
        ran_list.append(random.randint(0, lim))
        
    return ran_list

def gen_target(limit = constants.MAX_VALUE):
    return random.randint(0, limit)
