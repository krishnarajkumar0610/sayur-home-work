# problem #4
# write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab 
# abcd is  not same as cdba

# 123456 = 456123
# 123456 not = 412356
# hint - 
# there are many simple answers. you can try with slice function

# method 1 

String_one = input("Enter word one : ")   # asking user to give String 1

String_two = input("Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : ")   # asking user to give String 2

tempWord=String_one                     # creating temporary variable to store String one

b = False                               # assigning b as false

if(len(String_one)!=len(String_two)):   # if both String has different lenght we can't find the output
    print(f"Both Strings length are not same. String 1 length {len(String_one)} and String 2 length is {len(String_two)}")
    print(exit(0))                      # exiting from the program
    
for i in range(1,len(String_one)+1):    # This for loop is to traverse the String 1
    store_word=slice(1,len(tempWord)) 
    # sayur
    tempStr=tempWord[store_word]+tempWord[0]    # each time slicing the string and store it in temp String 
    if(tempStr in String_two):          # checking the sliced String is same as String 2
        print(f"Both Strings are same at {i}th time") # if the Strings are same then it is the output
        b=True                          # assigning True to b because we found the String to assigning True
        break                           # Then don't need to traverse the String to exiting from the loop
    
    tempWord=tempStr                    # each time storing the sliced String to the temp word to find next String
    
if(not b):  
                                        # if my b variable has False then we did't find the String so we need to tell that and 
                                        #i used not operator to change it as true to print the startement
    print(f"Both String has different characters. String 1 : {String_one} and String 2 : {String_two}")
    
    
#---------------------------------------------------------------------------------------------------------------------  
# method 2    
    
# String_one = input("Enter word one : ")   # asking user to give String 1
# String_two = input("Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : ")   # asking user to give String 2
# tempWord=String_one                     
# b = False                               

# if(len(String_one)!=len(String_two)):   
#     print((f"Both Strings length are not same. String 1 length {len(String_one)} 
#            and String 2 length is {len(String_two)}"))
#     print(exit(0))                      
    
# for i in range(1,len(String_one)+1):    
#     tempWord=tempWord[1:]+tempWord[0]   
#     if(tempWord in String_two):         
#         print(f"Both Strings are same at {i}th time") 
#         b=True                         
#         break                          
    
# if(not b):                                                                          
#     print(f"Both String has different characters. String 1 : {String_one} and String 2 : {String_two}")
  
    
# str 1 = "krishna"
# str 2 = "shnakri"
# "rishna"+"k"
# "ishnak"+"r"
# "shnakr"+"i"


    
    
#---------------------------------------------------------------------------------------------------------------------  

#method 3    
# String_one = input("Enter word one : ")   # asking user to give String 1

# String_two = input("Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : ")   # asking user to give String 2

# b = False                               # assigning b as false

# if(len(String_one)!=len(String_two)):   # if both String has different lenght we can't find the output
#     print(f"Both Strings length are not same. String 1 length {len(String_one)} and String 2 length is {len(String_two)}")
#     print(exit(0))                      # exiting from the program
    
# String_one+=String_one

# if(String_two in String_one):
#     print("Both String are same")
#     b=True
    
# if(not b):  
#                                         # if my b variable has False then we did't find the String so we need to tell that and 
#                                         #i used not operator to change it as true to print the startement
#     print(f"Both String has different characters. String 1 : {String_one} and String 2 : {String_two}")
    
# # outputs 

# # Enter word one : sayur learning
# # Enter the word two (eg: STR 1:abcde , STR 2: bcdea) :  learningsayur
# # Both Strings are same at 5th time

# # Enter word one : 123456
# Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : 456123
# Both Strings are same at 3th time

# Enter word one : 123456
# Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : 412356
# Both String has different characters. String 1 : 123456 and String 2 : 412356

# Enter word one : abcd
# Enter the word two (eg: STR 1:abcde , STR 2: bcdea) : cdab
# Both Strings are same at 2th time

# Both String has different characters. String 1 : abcd and 
# String 2 : cdba