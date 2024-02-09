import sys
import execution_time_algorithm
import algorithms


#if __name__ == "__main__":
table = execution_time_algorithm.take_execution_time(50000,100000,5000,5)
for row in table:
    print(row)
