word = input("Enter a word: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in word:
    if char.lower() in vowels:
        count += 1

print("Number of vowels:", count)