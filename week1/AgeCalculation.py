'''
Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name.
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.
'''


def agecalculation():
    name = input("Enter your name :") # asking user name
    print("Hello ",name)
    current_year=int(input("Enter current year :"))  # asking current year from user
    date_of_birth=int(input("Enter the year you are born  :"))   # asking user date of birth
    age=current_year-date_of_birth      # eg:   2023 - 2003 = 20
    # age will be stored in age variable 
    return "You are "+str(age)+" years old" # returned as string

print(agecalculation()) # printing the returned statement