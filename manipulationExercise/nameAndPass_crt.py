# Check if the username and password is correct. 
#      Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
#      passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
#      name of the company mentioned in the username, followed by any 3 numbers.
#      eg username : myname@sayur.com. password - mnamesay123

name = input("Enter your name & contain the char @ and .com or .edu or .tech or org at the end :")
password=input("Enter your password : ")
special_char = "@"  # initializing special character "@"
name_conditions=[".com",".edu",".tech","org"]  # initialing all conditions we need 
first_let=name[0]
third_let=name[2]
lastThree_let=""
company_name="sayur"
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
    reference_password=first_let+third_let+lastThree_let+company_name[:3]+"123"
    if password in reference_password:
        print(f"It is valid user name {name} and valid password  {password}") 
    else:
        print(f"Not a valid password {password}")        
else:
    print(f"It is not perfect user name {name} so cant generate password")
    
# OUTPUT
# It is perfect user name myname@sayur.com and password is mnamesay123        