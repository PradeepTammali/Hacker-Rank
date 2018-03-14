#!/bin/python

import re 

if __name__ == "__main__":
    n = input()
    pattern = re.compile(r'^[789]\d{9}$')
    for i in range(int(n)):
        number = input()
        if re.match(r'^[789]\d{9}$',str(number)):
            print('YES')
        else:
            print('NO')