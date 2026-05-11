number = 36
count = 0

for index in range(1, number + 1):
    if number % index == 0:
        count += 1
print("Divisor count of", number, ":", count)
