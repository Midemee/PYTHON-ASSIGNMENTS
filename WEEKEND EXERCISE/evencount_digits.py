number = 4578652
temporary = number
even_sum = 0

while temporary > 0:
    digit = temporary % 10
    if digit % 2 == 0:
        even_sum += digit
    temporary = temporary // 10

print("Sum of even Digits:", even_sum)
