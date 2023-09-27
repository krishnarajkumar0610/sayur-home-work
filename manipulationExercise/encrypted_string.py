# Input is an encrypted  string where there will be chars followed by number. The way to decrypt is 
# to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special 
# chars, all the chars between the number and special char are ignored.
#  eg - ac2bd3 means acacbdbdbd. 

encry_string = input("Enter the encrypted string : ")   # asking the user to enter the String
word="" # initializing the word variable to store the letters of the String

answer=[]
for i in range(len(encry_string)):  
    
    spec_char = ord(encry_string[i])    # converting each chars as acssi value
    
    if (spec_char>= 33 and spec_char <=47) or (spec_char >=58 and spec_char <=64):  
        # checking each chars wheather it is special char or not
        word=""
        continue        
    
    elif encry_string[i].isdigit():        # checking each letter is digit or not. if digit it is true
        
        num = int(encry_string[i])  # converting into number and stored in num
        
        answer.append(word*num) # printing the letters stored in word variable with num of times 
        
        word=""             # again changing it into empty String
        
    else:   # is not digit then it is character so adding the letter to word variable   
        word+=encry_string[i]


# OUTPUT

# Enter the encrypted string : ac2bd3
# acacbdbdbd

print(answer)