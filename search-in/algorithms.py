# 1st algorithm : Linar search method

def linear_search (array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return print("Target not found")

#2nd algorithm : Binary search method

def binary_search (array, target):
    return