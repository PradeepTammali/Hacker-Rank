#!/bin/python

import os
import sys
import heapq

def maximumProfit(profits, n):
    profit = -10000000
    profits.reverse()
    max_k = (n - (profits.index(max(profits)))) - 1
    profits.reverse()
    for index in range(max_k):
        if index != (max_k-1):
            if profits[index] < profits[index+1] < profits[max_k]:
                new_profit = profits[index]*profits[index+1]*profits[max_k]
                if new_profit > profit:
                    profit = new_profit
    min_k = profits.index(min(profits))
    for index in range(min_k+1,n):
        if index != (n-1):
            if profits[min_k] < profits[index] < profits[index+1]:
                new_profit = profits[min_k]*profits[index]*profits[index+1]
                if new_profit > profit:
                    profit = new_profit
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = -1
    if len(p) == n:
        result = maximumProfit(p, n)
    else:
        print('length and values are not correct')
    fptr.write(str(result) + '\n')
    fptr.close()