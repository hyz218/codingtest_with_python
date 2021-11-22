#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    string = s.split(' ')
    st = ''
    for i in range(len(string)):
        string[i] = string[i].capitalize()
        st+=str(string[i])+' '
        
    return st

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
