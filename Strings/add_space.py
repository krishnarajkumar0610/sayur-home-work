########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = input("Enter your string :")
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):     # while loop will stop when i > length of input string  
    
    if(i==len(inputString)-1):      # this if condition is used when i==length of string -1 
        newString+=inputString[i]   # it add only the last character of the string it won't cause index out of range    
    else:
        newString = newString+inputString[i]+inputString[i+1]    # i add 1st and 2nd character of the string
        newString += " " #add space # it add space in the string 
    i+=2    # incrementing +2 in i variable
    
print (f"The new String is {newString}")

#OUTPUT 

# Enter your string :abcdefg
# The new String is ab cd ef g