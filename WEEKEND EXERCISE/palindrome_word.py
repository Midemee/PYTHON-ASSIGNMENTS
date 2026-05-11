word = "madam"
is_palindrome = True
length = len(word)

for index in range(length // 2):
    if word[index] != word[length - 1 - index]:
        is_palindrome = False
        break
                                
if is_palindrome:
    print("  Yes, it is a palindrome!")
else:
    print("  No, it is not a palindrome.")
