#!/bin/python

import os
import sys

def canModify(a, n):
    for i in range(n):
        b = a[:i] + a[(i+1):]
        correct = True
        for j in range(n-2):
            if b[j] > b[j+1]:
                correct = False
                break
        if correct:
            return 'YES'
    return 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    t = int(input())
    for case in range(t):
        n = int(input())
        a = list(map(int, input().rstrip().split()))
        result = canModify(a, n)
        fptr.write(result + '\n')
    fptr.close()