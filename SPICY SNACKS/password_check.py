'''PASSWORD CHECK
PSEUDOCODE

Ask the user to enter a password
Count the number of characters in the password
Check the character count:
Less than 1 is Invalid
Less than 6 is Weak
Greater than 6 but less than or equalto 10 isMedium
Greater than 10 isStrong'''

password = input("Enter your password: ")
character_count = 0
for character in password:
    character_count = character_count + 1

if character_count < 1:
    print("Password is Invalid")
elif character_count < 6:
    print("Password Strength: Weak")
elif character_count <= 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
