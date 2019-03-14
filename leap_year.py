def is_leap(year):
    leap = False
    
    divByFour = year%4
    divByFourHundred = year%400
    divByHundred = year%100

    if divByFour == 0: 
      if divByHundred == 0 and divByFourHundred == 0:
          leap = True
      elif divByHundred != 0 and divByFourHundred != 0:
          leap = True
          
    return leap

year = int(input())
print(is_leap(year))
