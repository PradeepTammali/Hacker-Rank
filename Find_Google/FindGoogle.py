#!/bin/python3

import os
import re
import sys



if __name__ == '__main__':
    string = input()

    if re.match(r'^(g|G)(o|O|0|\(\)|\[\]|\<\>)(o|O|0|\(\)|\[\]|\<\>)(g|G)(l|L|I)(e|E|3)$', string):
        print(True)
    else:
        print(False)
