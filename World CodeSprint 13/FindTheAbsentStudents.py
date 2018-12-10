#!/bin/python

import os
import sys

# Complete the findTheAbsentStudents function below.
def findTheAbsentStudents(n, a):
    results = []
    for i in range(0, n):
        if i+1 not in a:
            results.append(i+1)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = findTheAbsentStudents(n, a)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
