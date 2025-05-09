word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word1 = word1.lower().replace(" ", "")
word2 = word2.lower().replace(" ", "")

if len(word1) != len(word2):
    print("The second word is not an anagram of the first.")
else:
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    if sorted_word1 == sorted_word2:
        print("The second word is an anagram of the first.")
    else:
        print("The second word is not an anagram of the first.")
