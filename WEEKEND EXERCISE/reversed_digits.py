number = 45678
reversed = 0

while number > 0:
    last_digit = number % 10
    reversed = reversed * 10 + last_digit
    number = number // 10
    
print("reversed:", reversed)
