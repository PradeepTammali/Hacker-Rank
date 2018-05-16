#!/bin/python

import os
import sys

def maximumProfit(profits, n):
    profit = -10000000
    count = 0
    profits.reverse()
    max_k = (n - (profits.index(max(profits)))) - 1
    profits.reverse()
    for index in range(max_k):
        if index != (max_k-1):
            for sub_index in range(index+1,max_k):
                if profits[index] < profits[sub_index] < profits[max_k]:
                    new_profit = profits[index]*profits[sub_index]*profits[max_k]
                    if new_profit > profit:
                        count = -1
                        profit = new_profit

    # min_index = profits.index(min(profits))
    # while min_index != (n-1):
    #     min_k = profits.index(min(profits[min_index:]))
    for value in profits:
        if value < 0:
            min_k = profits.index(value)
            for index in range(min_k+1,n):
                if index != (n-1):
                    for sub_index in range(index+1,n):
                        if profits[min_k] < profits[index] < profits[sub_index]:
                            new_profit = profits[min_k]*profits[index]*profits[sub_index]
                            if new_profit > profit:
                                count = -1
                                profit = new_profit
        # min_index += 1
    if count == 0:
        return -1
    else:
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