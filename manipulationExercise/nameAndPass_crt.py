# Check if the username and password is correct. 
#      Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
#      passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
#      name of the company mentioned in the username, followed by any 3 numbers.
#      eg username : myname@sayur.com. password - mnamesay123 
# method 1

company_name=input("Enter your company name :") # enter the compant name
special_char = "@" # initializing special character "@"
while True:    
    name = input("Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :")
    first_let=name[0]   # taking the 0th index char of the compant name
    third_let=name[2]   # taking the 1st index char of the compant name
    lastThree_let=""    # initializing stiring variable for last 3 letters
    if name.rfind(special_char) and (name.endswith(".com") or name.endswith(".edu") or name.endswith(".tech") or name.endswith(".org")):
        # this if is 1st it checks "@" in the name and checks name ends with .com or .tech or .edu or .org 
        specialChar_index=name.rfind(special_char)  # storing the "@" char index
        lastThree_let=lastThree_let+name[specialChar_index-3:specialChar_index] 
        # storing thr last 3 chars of the name before the char of "@"
        print("While giving password you must give like 1st char of your name,3rd char,and last 3 chars of name before @ special char, 1st 3 chars of your compant name and ends with any three number")
        password=input("Enter your password : ")    # entering the password
        reference_password=first_let+third_let+lastThree_let+company_name[:3]+password[-3:]  
        # it automatically generate the password
        if password in reference_password:  # if password is same as reference password
            print(f"Correct username {name}")   # user name and password are correct
            print(f"Correct password {password}")
            break
        else:
            print(f"Incorrect password {password}. Try again") # password is wroung but name is correct            
    else:
        print(f"Not a valid user name {name}. Try again")  
        # when name not contains @ or ends with .com or .tech or .edu or .org it is invalid name
        
    
# OUTPUT
# Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :krishna@gmail.com
# Enter your company name :sayur
# While giving password you must give like 1st char of your name,3rd char,and last 3 chars of name before @ special char, 1st 3 chars of your compant name and ends with any three numberEnter your password : kihnasay360
# Correct username krishna@gmail.com
# Correct password kihnasay360



    
# method 2    

name = input("Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :")
special_char = "@"  # initializing special character "@"
first_let=name[0]
third_let=name[2]
lastThree_let=""
name_conditions=[".com",".edu",".tech",".org"]
company_name=input("Enter your company name :")
check_name=False
for i in range(len(name)):
    if name[i] in special_char:
        lastThree_let=lastThree_let+name[i-3:i]
        for j in range(i,len(name)):
            if name[j]== ".":
                if name[j:] in name_conditions:
                    check_name=True;
                    break
        break
if check_name:
    password=input("Enter your password :")
    reference_password=first_let+third_let+lastThree_let+company_name[:3]+password[-3:]    
    if password in reference_password:
        print(f"It is valid user name {name} and valid password  {password}") 
    else:
        print(f"Not a valid password {password}")        
else:
    print(f"It is not perfect user name {name} so cant generate password")

#OUTPUT  
# Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :krishna@gmail.com
# Enter your company name :sayur
# Enter your password :kihnasay123
# It is valid user name krishna@gmail.com and valid password  kihnasay123    