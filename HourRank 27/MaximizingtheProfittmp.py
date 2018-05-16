#!/bin/python

import os
import sys
import heapq

def maximumProfit(profits, n):
    profit = -1
    new_profit = -1
    p = []
    for i in range(len(profits)):
        if i != len(profits)-1:         
            if profits[i] < max(profits[i+1:]):
                p.append(profits[i])
                if len(heapq.nlargest(2, profits[i+1:])) == 2:
                    if (profits[i+1:].index(heapq.nlargest(2, profits[i+1:])[0]) + i + 1) > (profits[i+1:].index(heapq.nlargest(2, profits[i+1:])[1]) + i + 1):
                        for value in p:
                            new_profit = value*heapq.nlargest(2, profits[i+1:])[0]*heapq.nlargest(2, profits[i+1:])[1]
                            if new_profit > profit:
                                profit = new_profit
            if profits[i] > min(profits[i+1:]):
                p.append(profits[i])
                if len(heapq.nsmallest(2, profits[i+1:])) == 2:
                    if (profits[i+1:].index(heapq.nsmallest(2, profits[i+1:])[0]) + i + 1) < (profits[i+1:].index(heapq.nsmallest(2, profits[i+1:])[1]) + i + 1) < i:
                        for value in p:
                            new_profit = value*heapq.nsmallest(2, profits[i+1:])[0]*heapq.nsmallest(2, profits[i+1:])[1]
                            if new_profit > profit:
                                profit = new_profit
    return profit

if __name__ == '__main__':
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    inp = input()
    p = list(map(int, inp.rstrip().split()))
    result = maximumProfit(p, n)
    fptr.write(str(result) + '\n')
    fptr.close()