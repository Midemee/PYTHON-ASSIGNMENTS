'''LARGEST NUMBER
PSEUDOCODE

collect three numbers
Assume first is the largest
compare second and third numbers against the largest
Print largest'''

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

largest = first

if second > largest:
    largest = second

if third > largest:
    largest = third

print("Largest number =", largest)

