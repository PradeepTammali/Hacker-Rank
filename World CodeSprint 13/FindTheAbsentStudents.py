#!/bin/python

import os
import sys

# Complete the findTheAbsentStudents function below.
def findTheAbsentStudents(n, a):
    # Return the list of student IDs of the missing students in increasing order.

    return 0

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = findTheAbsentStudents(n, a)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
