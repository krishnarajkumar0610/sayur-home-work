########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowel, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter the string : ")
inputSentence=inputSentence.lower()
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']
words=inputSentence.split(" ")
sentence=""
for word in words: #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = 0
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
        if char in vowels:
            first_vowel_index = index
            break
    # here using string slicing to add words in sentence
    '''word[first_vowel_index+1:] is store remaining letters from words after the index+1 '''
    '''word[:first_vowel_index + 1] is stores the letters from words before the index+1 '''
    sentence = sentence + word[first_vowel_index+1:] +word[:first_vowel_index + 1] + pigLatinKey    # finally adding the ay at end
    sentence+=" "   # adding space at end of each word
print(f"Final sentence is {sentence}")

# OUTPUT

# Enter the string : I am Python
# Final sentence is iay maay npythoay 