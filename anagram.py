def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

word1 = input("Enter a word : ")
word1 = str(word1)
word2 = input("Enter a word : ")
word2 = str(word2)

print(anagram(word1,word2))