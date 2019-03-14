#!/bin/python3
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 21, print Not Weird
N = int(input())
rem = N%2 
if (rem == 0) and (N >= 2 and N <= 5):
  print("Not Weird")
elif (rem == 0) and (N >= 6 and N <= 20):
    print("Weird")
elif (rem == 0) and (N >= 21):
    print("Not Weird")
else:
    print("Weird")

