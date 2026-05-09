'''LEAP YEAR
PSEUDOCODE

Ask the user to enter a year
Check if the year is divisible by 400, its a leap year
Else check if the year is divisible by 100, its not a Leap Year
Else check if the year is divisible by 4, it is Leap Year
else Not a Leap Year'''


year = int(input("Enter a year: "))

if((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} is a leap year")
    
else:
    print(f"{year} is not a leap year")
