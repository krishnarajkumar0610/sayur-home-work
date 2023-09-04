######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

import random
computerNo = random.randint(3, 9)

attempt = 0
while(True):
    userNo = int(input("Enter your guessing number :"))
    if userNo==computerNo:
        break
    elif userNo>computerNo:
        print(f"user guess {userNo} - High number ")
    elif userNo<computerNo:
        print(f"user guess {userNo} - Low number ")            
    attempt +=1

print (f"User guessed the number in {attempt} attempts and the correct number is {computerNo}")