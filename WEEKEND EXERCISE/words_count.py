sentence = "Hi, My Name Is Aramide"
word_count = 0
in_word = False

for character in sentence:
    if character != ' ':
        if in_word == False:
            word_count = word_count + 1
            in_word = True
    else:
        in_word = False

print("No of Words:", word_count)
