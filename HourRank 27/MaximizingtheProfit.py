#!/bin/python

import os
import sys
import heapq

def maximumProfit(profits):
    profit = -1
    new_profit = -1
    for i in range(len(profits)):
        if i != len(profits)-1:   
            print(i)          
            if profits[i] < max(profits[i+1:]):
                p = profits[i]
                if len(heapq.nlargest(2, profits[i+1:])) == 2:
                    if profits.index(heapq.nlargest(2, profits[i+1:])[0]) > profits.index(heapq.nlargest(2, profits[i+1:])[1]):
                        print(heapq.nlargest(2, profits[i+1:])[0], heapq.nlargest(2, profits[i+1:])[1], p)
                        new_profit = p*heapq.nlargest(2, profits[i+1:])[0]*heapq.nlargest(2, profits[i+1:])[1]
                        if new_profit > profit:
                            profit = new_profit
                            # print('profit', profit)
                        # break
    return profit


if __name__ == '__main__':
    fptr = open(os.environ['PWD']+'/output.txt', 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split(   )))
    result = maximumProfit(p)
    fptr.write(str(result) + '\n')
    fptr.close()