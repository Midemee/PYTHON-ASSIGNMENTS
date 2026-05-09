'''DIVISION
PSEUDOCODE

Input first number
Input second number
If second number is not equal to 0, Divide first number by second number and Print result
Else, Print cannot divide by zero'''

first_number = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))

if second_number != 0:
    print("Result =", first_number / second_number)
else:
    print("Cannot divide by zero")

