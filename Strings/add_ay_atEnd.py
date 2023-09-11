########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter your sentence :")
pigLatinKey = 'ay'
sentecnces=inputSentence.split(" ")
sentence=""
count=0
b=True
for word in sentecnces: #gets the word in a sentence
    #take the first char
    firstChar = word[0] # storing the 1st character from the word into firstChar variable  
    sentence = sentence+ word[1:] + firstChar + pigLatinKey
    sentence+=" "    
   
print(f"Final sentence is {sentence}") #FillinMissingCode)
        