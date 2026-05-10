number = int(input("Enter a number: "))
for rows in range(number+1):
    for cols in range(rows):
        print("*", end=" ")
    print()
