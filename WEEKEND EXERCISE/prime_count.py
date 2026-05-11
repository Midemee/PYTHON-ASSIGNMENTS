prime_count = 0

for num in range(2, 101):
    is_prime = True

    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1

print("Count:", prime_count)
