# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS

def reverse(word):  # this function is to return the reversed word
    return word[::-1]  # reversing the word and returning it

sentence = input("Enter a sentence : ").split(' ')  # asking the user input and spliting it

for index,word in enumerate(sentence):   # this loop is to get each value from the list
    result = reverse(word)  # calling reverse function and storing the returned value in result variable
    print(result,end=' ')   # printing the reversed word
    
    
# output
# Enter a sentence : I am Sayur
# I ma ruyaS 