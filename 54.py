sentence = input("Enter a sentence: ")
vowel_count = 0
for char in sentence:
    char_lower = char.lower()
    if char_lower in 'aeiou':
        vowel_count += 1

print("Number of vowels:", vowel_count)

