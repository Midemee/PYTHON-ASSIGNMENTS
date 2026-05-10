number = int(input("Enter a number: "))
for count in range(1, number+1):
    result = number * count
    print(number, "x", count, "=", result)
