number = 442
temporary = number
reversed = 0

while temporary > 0:
    last_digit = temporary % 10
    reversed = reversed * 10 + last_digit
    temporary = temporary // 10

if number == reversed:
    print("  Yes, it is a palindrome!")
else:
    print("  No, it is not a palindrome.")
