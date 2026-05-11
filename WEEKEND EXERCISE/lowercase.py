sentence = "Hi, My Name Is Aramide"
count = 0

for character in sentence:
    if character >= 'a' and character <= 'z':
        count += 1

print("Lowercase Count:", count)
