'''are you teacher or student?
get their name
if they are in the final year?
do you teach final year students?
if they are in the final year or if they teach final year students. welcome to the final year
if they are a teacher, Hello teacher name
if they are student , Hello student name'''

name = input("Enter your name :")
name=name.lower()

role = input("Enter the role of you in college :")
role=role.lower()

if role !="student" and role !="teacher":
    print("Enter valid role of you in college")
    
elif role=="student":
    print("You are final year student ?")
    decission = input("Enter Yes or No :")
    decission=decission.lower()
    if decission=="yes":
        print(f"Hello {name} welcome to final year")
    else:
        print(f"Thanks for your information")
        
elif role=="teacher":
    print(f"Hello {name}")
    print("do you teach for final year students ?")
    teach=input("Enter yes or no :")
    teach=teach.lower()
    if teach=="yes":
        print("Welcome to final year")
    else:
        print(f"Thanks for your time next year please take for final year students")