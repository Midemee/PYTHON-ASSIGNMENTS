decimal_number = 13
binary_result = ""
temporary = decimal_number

while temporary > 0:
    remainder = temporary % 2
    binary_result = str(remainder) + binary_result
    temporary = temporary // 2
)
print(decimal_number, "to Binary:", binary_result)
