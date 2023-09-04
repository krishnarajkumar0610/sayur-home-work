'''Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov"'''
message = input("Enter the message :")
pattern="*** **** ** **********     *****"
final_message=''
message=message.replace(" ","")  # here i revomed the spaces and stored in the same variable message
index=0
for i in range(len(pattern)):
        
    if pattern[i]=="*":  # if char is * i add character from message in final_message variable
        final_message=final_message+message[index]
        index=index+1
    
    elif pattern[i]==" ":   # if char is " " i add " "  in final_message variable
        final_message=final_message+" "
    
    if index==len(message):  
        index=0
''' if my index number is equal to my message length i change index =0 because if it increase more than message length 
it occurs index out of bound'''
    
    
print(f"Pattern : {pattern}")
print(f"Encoded : {final_message}")