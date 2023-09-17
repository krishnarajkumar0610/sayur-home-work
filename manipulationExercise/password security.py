#  Print the level of the password security and if the password is acceptable
#  Weak - only alphabets or only numbers or only special chars
#  Ok - at least one alphabet, one number and one special char
#  strong - at least three alphabets, two numbers and one special char
#  Very strong - same as strong, but at least 16 count
# All passwords must be at least 8 chars long. You can use RegEx if you want.

pass_length=0
count_alph,count_nums,count_spec=0,0,0
while True:
    password=input("Enter password (note : it length should be 8 or >8 and atleast <=16 : ")  
    pass_length=len(password)   # storing the lenght of the password
    if pass_length>=8:  # if length is >=8 then i can set password 
        for i in range(len(password)):  # this loop for check every character it is int or char or special char
            charNum=int(ord(password[i]))
            if password[i].isalpha():   # is char
                count_alph+=1    # +1 in count alpha
            elif password[i].isdigit(): # is number
                count_nums+=1   # +1 in count number
            elif charNum>=33 and (charNum<=47 or charNum>=58 and charNum<=64):  # is special character
                count_spec+=1   # +1 in count special char
        break
    else:   # if length is <8
        print(f"Password is lessthan 8 characters. Try again") 
        
if count_alph==1 and count_nums==1 and count_spec==1:   # if alpha and num and spec char contains only 1 of each password is "OK"
    print(f"Your password is ok")
elif (count_alph>1 and count_alph<=3) and (count_nums>1 and  count_nums<=2 and count_spec>=1):
    # when alpha count  > 1 and alpha count <=3 and num count >1 and  num count <=2 and spec char >=1 then it is strong password
    print(f"Password is strong")
else:
    print(f"Your password only contains {password}. Not having mixed characters,integers,special characters")
    exit(0)
if len(password)>=16:   # if lenght is 16 it is strong password
    print(f"Password is very strong and its length is {len(password)}")
elif len(password)==8:
    print(f"Password is strong and its length is {len(password)}")
print("-"*30)
print(f"Number of alphas in password is {count_alph}")
print(f"Number of digits in password is {count_nums}")
print(f"Number of special chars in password is {count_spec}")
print("-"*30)