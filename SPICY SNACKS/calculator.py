'''CALCULATOR
PSEUDOCODE

Ask the user to enter the first number
Ask the user to enter the second number
Ask the user to enter an operator (+, -, *, /)
Check which operator was entered:
If + add the two numbers and print result
If - subtract the two numbers and print result
If "*" multiply the two numbers and print result
If "/" check if second number is 0, print error message division cant be done with 0, 
if not 0, divide and print result
If none of the above, print message invalid operator message'''


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
    print(first_number, "+", second_number, "=", result)

elif operator == "-":
    result = first_number - second_number
    print(first_number, "-", second_number, "=", result)

elif operator == "*":
    result = first_number * second_number
    print(first_number, "*", second_number, "=", result)

elif operator == "/":
    if second_number == 0:
        print("Error: You cannot divide by zero!")
    else:
        result = first_number / second_number
        print(first_number, "/", second_number, "=", result)

else:
    print("Invalid operator! Please use +, -, *, or /")
