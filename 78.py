sentence = input("Enter a sentence: ")

count = 0

for char in sentence:
    if char == " ":
        count += 1

print("Number of blank spaces:", count)