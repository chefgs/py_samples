# arithmetic 
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum = a + b
    print(str(sum))

    if b < a:
      diff = a - b
      print(str(diff))
    else:
      print("Difference: Input b is greater than a. So output will be in negative, hence ignored")
    
    prod = a * b
    print(str(prod))


