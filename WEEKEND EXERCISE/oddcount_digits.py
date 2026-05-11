number = 4578652
temporary = number
odd_sum = 0

while temporary > 0:
    digit = temporary % 10
    if digit % 2 != 0:
        odd_sum += digit
    temporary = temporary // 10

print("Sum of odd Digits:", odd_sum)
