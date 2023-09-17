# ########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit

# method 1

name = input("Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :")
special_char = "@"  # initializing special character "@"
first_let=name[0]
third_let=name[2]
lastThree_let=""
company_name=input("Enter your company name :")
check_name=False
if name.rfind(special_char) and (name.endswith(".com") or name.endswith(".edu") or name.endswith(".tech") or name.endswith(".org")):
    specialChar_index=name.rfind(special_char)
    lastThree_let=lastThree_let+name[specialChar_index-3:specialChar_index]
    print("While giving password you must give like 1st char of your name,3rd char,and last 3 chars of name before @ special char, 1st 3 chars of your compant name and ends with any three number")
    password=input("Enter your password : ")
    reference_password=first_let+third_let+lastThree_let+company_name[:3]+password[-3:]
    if reference_password in password:
        print(f"Correct username {name}")
        print(f"Correct password {password}")
    else:
        print(f"Incorrect password {password}")
else:
    print(f"Not a valid user name {name}")
    print(exit(0))
    
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