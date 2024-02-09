import sys
import execution_time_algorithm
import algorithms


#if __name__ == "__main__":
table = execution_time_algorithm.take_execution_time(1000000,10000000,1000000,3)
for row in table:
    print(row)
