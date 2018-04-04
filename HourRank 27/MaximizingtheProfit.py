#!/bin/python

import os
import sys

def maximumProfit(p):
    print(p)
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split(   )))
    result = maximumProfit(p)
    fptr.write(str(result) + '\n')
    fptr.close()
