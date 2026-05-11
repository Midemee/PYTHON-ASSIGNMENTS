count = 0
for number in range(2, 101):
    is_prime = True

    for divisor in range(2, num):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()
