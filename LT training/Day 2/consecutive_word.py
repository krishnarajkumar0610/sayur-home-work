# Problem #2
# Write a program that reads a passage or string and 
# counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but 
# not "apple orange apple."

# sample input = It is true for all that that that  refers to is not the same that that  refers to



def checkCons(sentence):    # this method is to find the consecutive count
    
    count = 0   # assigning the count as 0
    for index in range(len(sentence)):  # this for loop is to traverse the list
        if index==len(sentence)-1:  # if my index is reached at lat i can't find the other consecutive to ending to check the consecutive
            return count    # then returning the consecutive count
        
        elif sentence[index] in sentence[index+1]:  # other wise checking the 1st and 2nd word is consecutive or not if it is then counting it
            count+=1
    
sentence = input("Enter the sentence : ").split(' ')    # asking input from the user and spliting it by space

cons_count=checkCons(sentence)  # storing the consecutive count  from the function call

print(f"In this sentence the consecutive count is {cons_count}") 


# output

# Enter the sentence : hi i am krishna krishna is best student student krishna is best best student in sayur 
# In this sentence the consecutive count is 3