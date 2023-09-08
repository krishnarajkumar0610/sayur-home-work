'''Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)'''
name_one=input("Enter name 1 :")    # asking user name one

name_two=input("Enter name 2 :")    # # asking user name two

if(len(name_one)==len(name_two)):
    print("Already both length are equal")
else:
    while(length_name_one!=length_name_two):
        if length_name_one<length_name_two:
            name_one=name_one+'a'
            length_name_one=len(name_one)
        elif length_name_one>length_name_two:
            name_two=name_two+'a'
            length_name_two=len(name_two)
print(f"name one :{name_one}")
print(f"Name two :{name_two}")



# OUTPUT
# Enter name 1 :krishna
# Enter name 2 :raj kumar
# name one :krishnaaa
# Name two :raj kumar