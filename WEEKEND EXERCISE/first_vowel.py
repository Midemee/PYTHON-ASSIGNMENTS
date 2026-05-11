word = "Travelling"
vowels = "aeiouAEIOU"
first_vowel = -1

for index in range(len(word)):
    character = word[index]
    for vowel in vowels:
        if character == vowel:
            first_vowel = index
            break
    if first_vowel != -1:
        break

print("First Vowel:", first_vowel,
      "Character:", word[first_vowel])
