#!/bin/python3

import os
import sys
from functools import reduce
from operator import mul
import math 

# Complete the howManyGoodSubarrays function below.
def howManyGoodSubarrays(A, m, k):
    # Return the number of good subarrays of A.
    # Finding all the subarrays
    count = 0
    n = len(A)
    for i in range(0, n):
        # if k != 0 and A[i] == 0:
        #     continue
        # elif k == 0 and A[i] == 0:
        #     if i <= int(n/2):
        #         index = i+1
        #     else:
        #         index = (n - (i+1))+1
        #     count += index*(n - (index-1))
        # else:
        for j in range(i, n):
            if k != 0 and (0 in A[i:j+1]):
                continue
            elif k == 0 and (0 in A[i:j+1]):
                count += 1
            elif reduce(mul, A[i:j+1]) % m == k:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        nmk = input().split()
        n = int(nmk[0])
        m = int(nmk[1])
        k = int(nmk[2])
        A = input()
        result = howManyGoodSubarrays(A, m, k)
        fptr.write(str(result) + '\n')
    fptr.close()
