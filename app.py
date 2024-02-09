import sys
from search_in_array import  algorithms
from search_in_array import execution_time_algorithm

#if __name__ == "__main__":
table = execution_time_algorithm.take_execution_time(1000,10000,500,5)
for row in table:
    print(row)
