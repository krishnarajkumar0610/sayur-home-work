#  Print the level of the password security and if the password is acceptable
#  Weak - only alphabets or only numbers or only special chars
#  Ok - at least one alphabet, one number and one special char
#  strong - at least three alphabets, two numbers and one special char
#  Very strong - same as strong, but at least 16 count
# All passwords must be at least 8 chars long. You can use RegEx if you want.

count=0
count_alph,count_nums,count_spec=0,0,0
while True:
    password=input("Enter password (note : it length should be 8 or >8 and atleast <=16")
    for i in range(len(password)):
        count+=1
    if count>=8:
        for i in range(len(password)):
            charNum=int(ord(password[i]))
            if password[i].isalpha():
                count_alph+=1
            elif password[i].isdigit():
                count_nums+=1
            elif charNum>=33 and (charNum<=47 or charNum>=58 and charNum<=64):
                count_spec+=1
        break
    else:
        print(f"Password is lessthan 8 characters. Try again")
if count_alph==1 and count_nums==1 and count_spec==1:
    print(f"Your password is ok")
elif (count_alph>1 and count_alph<=3) and (count_nums>1 and  count_nums<=2 and count_spec>=1):
    print(f"Password is strong")
if len(password)>=16:
    print(f"Password is very strong and its length is {len(password)}")
elif len(password)==8:
    print(f"Password is strong and its length is {len(password)}")
print(f"Number of alphas in password is {count_alph} \n Number of digits in password is {count_nums} \n Number of special chars in password is {count_spec}")