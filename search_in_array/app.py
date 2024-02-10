import sys
import execution_time_algorithm
import algorithms


#if __name__ == "__main__":
#table = execution_time_algorithm.take_execution_time(1000000,10000000,1000000,100)
table = execution_time_algorithm.take_execution_time(100000,1000000,100000,10)
for row in table:
    print(row)
