Year = 2029

if (Year % 4 == 0) or (Year % 400 == 0 and Year % 100 != 0):
    print(Year, "Year is a leap year") 
else:
    print(Year, "Year is not a leap year")