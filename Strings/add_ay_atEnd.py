########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter your sentence :")
pigLatinKey = 'ay'
sentecnces=inputSentence.split(" ")
sentence=""
for word in sentecnces: #gets the word in a sentence
    #take the first char
    firstChar = word[0] # storing the 1st character from the word into firstChar variable
    if (word.isalpha()):   
        sentence = sentence+ word[1:] + firstChar + pigLatinKey 
        # adding the words from 1st index to end + first char of word + ay
        sentence+=" " # adding space at end of each word
        
    else:   # if word contains numbers or some special character it won't perform if condition 
        print("*"*10)
        print(f"{word} contains numbers in this word")   
        print("*"*10)
        print()
        
print()        
print("-"*10)
print(f"Final sentence is {sentence}") #FillinMissingCode)
print("-"*10)
        
        
#OUTPUT
# Enter your sentence :I am Python

# ----------
# Final sentence is Iay maay ythonPay 
# ----------