
# 2. From a given passage find the longest and shortest word 
# and print the same. Accept the passage as an input from user



sentence = input("Enter a sentence : ")

sentence = sentence.split() # Split the passage into words

# Initialize variables to store the longest and shortest words
longest_word = sentence[0]
shortest_word = sentence[0]

# Iterate through the words to find the longest and shortest words
for word in sentence:
    if len(word) > len(longest_word):   # if length of the word is > longest word 
        longest_word = word # changeing word as long word
    elif len(word) < len(shortest_word):    # if length of the word is < short word
        shortest_word = word    # changing word as short word

print(f"Longest word: {longest_word}")
print(f"Shortest word:{ shortest_word}")

# OUTPUT :-

# Enter a sentence : From a given passage find the longest and shortest word 
# Longest word: shortest
# Shortest word:a