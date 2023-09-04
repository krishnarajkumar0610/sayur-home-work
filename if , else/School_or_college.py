'''
    Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name 
and print 'Hello', user's name. 
Ask what year they were born.  
eg Hello Chitra, what year were you born?
get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college, based on users age. 
(hint - use if/elif)
'''
def find_school_or_college(age,name):

        
    if age>=5 and age<=10: 
        print(f"{name} you are currently going to elementary school and your age is {age}")
        
    elif age>10 and age<=15: 
        print(f"{name} you are currently going to middle school and your age is {age}")
        
    elif age>15 and age<=17: 
        print(f"{name} you are currently going to highschool and your age is {age}")
        
    elif age>17 and age<=21:
        print(f"{name} you are currently going to college and your age is {age}")
        
name = input ("enter your name :")

print(f"Hello {name}")

# asking the user  birth year
born_year=int(input("what year were you born note : year should between 2000 to 2023\nborn year = "))  

age=2023-born_year

if  born_year<2000:
    print(f"Invalid year {born_year}")
elif age==0: 
    print(f"Invalid age {age}")
elif age>=1 and  age<=5:  # if my age is in between 1 to 5 i can't go to school
    print(f"You are not eligible for schooling because your age is {age} and it is lessthan 5")
else:
    find_school_or_college(age,name)