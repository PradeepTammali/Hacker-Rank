#!/bin/python

import os
import sys

#
# Complete the canModify function below.
#
def canModify(a):
    negative_element_count = 0
    for i in range(len(a[1:])):
        if a[i] > a[i+1]:
            negative_element_count += 1
    if negative_element_count <= 1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().rstrip().split()))
        result = canModify(a)   
        # print(result + '\n')
        fptr.write(result + '\n')
    fptr.close()