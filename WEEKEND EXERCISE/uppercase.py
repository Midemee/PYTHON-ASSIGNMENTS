sentence = "Hi, My Name Is Aramide"
count = 0

for character in sentence:
    if character >= 'A' and character <= 'Z':
        count += 1

print("Uppercase Count:", count)
