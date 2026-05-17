first = 0
second = 1

for index in range(20):
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number

print()

