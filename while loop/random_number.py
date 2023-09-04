######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random    # importing random from package

computerNo = random.randint(3, 9)   # storing the random number from 3 to 9

attempt = 0 # used to count the number of attempts to guess the number

while(True):# always running the loops until guessing the correct number
    
    attempt +=1
    userNo = int(input("Enter your guessing number :"))  # asking user to guess number
    
    if userNo==computerNo:  # if user guessed the correct number breaking the loops
        break
    
    elif userNo>computerNo: # if user guessed higher than computer number it print high
        print(f"user guess {userNo} - High number ")
        
    elif userNo<computerNo:# if user guessed low than computer number it print low
        print(f"user guess {userNo} - Low number ")            

print (f"User guessed the number in {attempt} attempts and the correct number is {computerNo}")
# printing the number of attempts and printing the computer number alsp