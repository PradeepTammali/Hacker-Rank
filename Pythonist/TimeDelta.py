#!/bin/python

import sys
import datetime

def time_delta(t1, t2):
    firstDate = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    secondDate = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs(firstDate - secondDate).total_seconds())

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)