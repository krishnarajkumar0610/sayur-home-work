'''Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)'''
name_one=input("Enter name 1 :")    # asking user name one

name_two=input("Enter name 2 :")    # # asking user name one

length_name_one=len(name_one)   # storing name one length

length_name_two=len(name_two)   # storing name two length

if(length_name_one==length_name_two):   # comparing 2 names length if it equals it true
    print("Already both length are equal")
    
else:   # if it is not equal it comes else statement
    while(length_name_one!=length_name_two):    # it stops when my both name one and name two length becomes equal
        if length_name_one<length_name_two: # if name one length < name two, add 'a' in name one at end
            name_one=name_one+'a'   # adding a at end in name one
            length_name_one=len(name_one)   # storing name one length
            
        elif length_name_one>length_name_two:   # if name two length < name one, add 'a' in name two at end
            name_two=name_two+'a'      # adding a at end in name one
            length_name_two=len(name_two)   # storing name one length
            
print(f"name one :{name_one}")
print(f"Name two :{name_two}")



# OUTPUT
# Enter name 1 :krishna
# Enter name 2 :raj kumar
# name one :krishnaaa
# Name two :raj kumar