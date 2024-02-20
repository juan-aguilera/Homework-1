# Homework-1
# About this repo

Simple python project to show a way to take experiental execution time to compare a set of algorithms (three in this case) in fair way.

## search in array algorithms

3 search in array algorithms (Linear search, binary search, ternary search)

### Problem statement
​
The sample problem is to take a list of array's and search a list of numbers within them, with  the following criteria:

* The input array's for binary search algorithm must be sorted. A default built-in python function inside the search algorithm, will be used for this propurse.
* The input array's for ternary search algorithm must be sorted. A default built-in python function inside the search algorithm, will be used for this propurse.
* The algorithm will only search within arrays of strings and arrays of numbers.  Alphanumeric arrays will not accepted. 
* These three algorithms will return the index of the first ocurrence of the string/number that they encounter. 

### Examples

* Find 3 in  `3 1 9 10 3` the output should be `0`

* Find 6 in  `1 9 8 2 3 4 5 7 6` the output should be `8`

* Find banana in  `"apple", "banana", "cherry", "date", "banana", "fig", "grape", "lemon"` the output should be `1`

* Find `120` in `10 90 80 20 30 40 50 70 60` the output should be `Target not found`


# Python version
Python 3.11.0
​
# Running locally and testing

* Note: This instructions are for Windows. Mac or linux may require some changes. 
* Note: If you have a script named test.bat that you want to execute on Mac/linux, you would need to convert it to a shell script file compatible with Mac/Linux. This often involves changing the syntax of commands and removing Unix-specific features. Additionally, you might need to adjust file paths to ensure they work correctly in the Mac/Linux environment.
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.bat`
* To try a default example, run: `: ./run.bat`. In the file ./run.bat is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

COVERAGE REPORT
-------------------------------------------------
algorithms.py                    36      8    78%
constants.py                      2      0   100%
data_generator.py                 9      0   100%
execution_time_algorithm.py      30      0   100%
running_file.py                  24      0   100%
unitest_plot.py                  10      0   100%
-------------------------------------------------
TOTAL                           111      8    93%

