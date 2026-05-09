def palindrome(number):
    string_number = str(number)
    if string_number == string_number[::-1]:
        return "Number is a palindrome"
    return "Number is not a palindrome"
    
def prime(number):
    for index in range(2, number):
        if number % index == 0:
            return "Number is not a prime number"
        return "Number is a prime number"
