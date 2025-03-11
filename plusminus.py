#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    for i in arr:
        if i>0:
            pos+=1
        if i<0:
            neg+=1
    zero = (n-pos-neg)/n
    pos = pos/n
    neg = neg/n
    
    print(f"{pos:.6f}")
    print(f"{neg:.6f}")
    print(f"{zero:.6f}")

#positive_count = sum(1 for x in arr if x > 0)
#positive_ratio = positive_count / n
#print(f"{positive_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
