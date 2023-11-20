# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the 
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump. 
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.


import random   # importing the class random    

point = 0   # assigning  0 to the point

winning_point = 50  # total winning point is 50

while(point!=winning_point):    # this while loop will run unitil my point reaches the winning point
    
    val=random.randint(0,6) # generating the random number from 0 to 6
    
    if val == 0:    # if my number is 0 then i can't continue the game
        break   # and coming out
    
    elif val % 2 == 0:  # if the number is even 
        point+=2    # adding +2 point in my point
        
    elif val % 2 !=0 and val == 1 or 3:    
        # if my number is odd then it is 1 or 3 
         continue   # then i want to skip to add the point
    
    elif val == 5:  # if my number is 5 then adding +5 to the point
        point+=3

if point == 0:
    print(f"You are duck out player haha, because your point is {point}")        
elif point==50:   # if my point is 50 then i am won        
    print(f"Total points are {point} and you are win")
else:   # if my point is not 50 then i am defeted
    print(f"Total points are {point} and you are defeted ")    
    
    
    
# output

# Total points are 4 and you are defeted 

# Total points are 50 and you are win 

# You are duck out player haha, because your point is 0 