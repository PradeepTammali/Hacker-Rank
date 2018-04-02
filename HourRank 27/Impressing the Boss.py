#!/bin/python

import os
import sys

def canModify(a):
    negative_element_count = 0
    for i in range(len(a[1:])):
        if i == 0:
            if a[i] > a[i+1]:
                a[i] = a[i+1] - 1
                negative_element_count += 1
        elif not (a[i-1] <= a[i] <= a[i+1]):
            if not (a[i-1] <= a[i]):
                a[i] = int((a[i-1]+a[i+1])/2)
            elif not (a[i] <= a[i+1]) and i+1 != len(a) - 1:
                a[i+1] = int((a[i]+a[i+2])/2)
            elif not (a[i] <= a[i+1]) and i+1 == len(a) - 1:
                a[i+1] = a[i]+ 1
            negative_element_count += 1
    if negative_element_count <= 1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().rstrip().split()))
        result = canModify(a)   
        # print(result)
        fptr.write(result + '\n')
    fptr.close()