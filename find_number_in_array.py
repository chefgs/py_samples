#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def findNumber(arr, k):
    if k in arr:
      return "YES"
    else:
      return "NO"

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()

# Input
# 1. Arrat count = Total number of array elements
# 2. arr = Array of numbers
# 3. k = element to be find
