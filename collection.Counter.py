#This code will solve this challenge https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

import sys
from collections import Counter
input_data = sys.stdin.read().splitlines()

x = int(input_data[0])
shoeSizes = Counter(map(int,input_data[1].split()))
n = int(input_data[2])
earning = 0
for i in range(3, 3+n):
    size, price = map(int, input_data[i].split())
    if shoeSizes[size]>0:
        earning+= price
        shoeSizes[size] -=1
  
print(earning)

"""
How It Works
  Reading Input from STDIN:
  
    All input is read at once using sys.stdin.read().
    Split the input into lines using .splitlines() for easier processing.
    First line: number of shoes.
    Second line: space-separated list of shoe sizes.
    Third line: number of customers.
    Subsequent lines: each customer's desired shoe size and price.
  Logic:
  
    Use a Counter to manage the inventory of shoe sizes.
    For each customer, check if the desired shoe size is available. If it is, add the price to earnings and decrement the inventory for that size.
    Output to STDOUT:
  
    The result (total earnings) is printed directly using print().
"""
