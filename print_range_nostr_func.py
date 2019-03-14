# Printing int range values without string function
import sys
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, sep='', end='', file=sys.stdout)

# Input
# 3
# Output
# 123
