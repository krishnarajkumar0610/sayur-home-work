# Problem 2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row,col) enter the player's initial. 
# If the player  A rolls the dice and  if  player B already has their initial in the same row,col
# add a point to A and change the initial to A. 

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions

import random   # importing the class random

def setStar(board,size):    # this method is to set star in the board
    for outer in range(size):   # this loops is to set star
        for inner in range(size):
            board[outer].append('*')  
            
def roll(): # this method is to generate row and col number
    num = random.randint(1,6)   # generating any number in between 1 to 6
    return  num-1   # returning it with -1

def display(board): # display the board 
    print('--------------------------------------------------')
    for outer in range(len(board)):
        for inner in range(len(board[outer])):
            print(f"| {board[outer][inner]} |",end=' ')
        print()
    print('--------------------------------------------------')
    
    
def play(board,player,row,col): # this method is to apply the initial of the player
    if board[row][col] == '*':     # if the particular position has * then apply the initial
        board[row][col] = player        
    elif board[row][col]!=player:   # if the particular position has other initial then apply current initial
        board[row][col]=player  
        display(board)
        return 1    # adding point to the player           
    display(board)  # displaying the board
    return 0        # adding 0 point

board = [ [],[],[],[],[],[] ]       # creating the 2D list
setStar(board,6)    # calling the set star method to set star in the board
point_A = 0 # creating point a to count point of A
point_B = 0 # creating point b to count point of B
players = ['k','s'] # players in the list   
while point_A!=5 and point_B!=5:    
    # his while loop will run if any one of the point reaches 5 it will stop
    index=0 # assigning 0 to index
    row=roll()  # calling roll() to get any number from 1 to 6 to store in row
    col=roll()  # calling roll() to get any number from 1 to 6 to store in col
    point_A+=play(board,players[index],row,col) # calling the play method and adding the returning point to point a
    index+=1    # incrementing the index
    row=roll()  # calling roll() to get any number from 1 to 6 to store in row
    col=roll()  # calling roll() to get any number from 1 to 6 to store in col
    point_B+=play(board,players[index],row,col) # calling the play method and adding the returning point to point b
    
if point_A==5:  # if point a is 5 
    print("Player A")   # Player A is winner
else:   # if point b is 5 
    print("Player B")   # Player B is winner
    
    
'''
output

--------------------------------------------------
| * | | * | | * | | * | | * | | * | 
| * | | * | | * | | * | | * | | * | 
| * | | * | | * | | * | | * | | * | 
| * | | * | | * | | * | | * | | * | 
| * | | * | | * | | k | | * | | * | 
| * | | * | | * | | * | | * | | * | 
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s | 
| * | | * | | * | | * | | * | | * | 
| * | | * | | * | | * | | * | | * | 
| * | | * | | * | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | * | | * | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| * | | * | | * | | * | | * | | * |
| * | | * | | * | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | * | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| * | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | * | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| k | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | * | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| k | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| k | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | * |
--------------------------------------------------
--------------------------------------------------
| * | | * | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | * | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | s | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | s | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | s | | * | | s |
| * | | * | | * | | * | | * | | * |
| s | | * | | * | | * | | * | | * | 
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | s | | * | | s |
| * | | * | | * | | k | | * | | * |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | * | | s | | * | | s |
| * | | * | | * | | k | | * | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | * | | * | | k | | * | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | * | | * | | k | | s | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | s | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | * | | * | | k | | s | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | k | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | k | | * | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | k | | k | | * | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | * | | * |
| * | | * | | k | | k | | s | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | * |
| * | | * | | k | | k | | s | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | * | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | * |
| * | | * | | k | | k | | s | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | * | | * | | k | | * | | * |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | * |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | s | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | * | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | s | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | k |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| * | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| * | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| k | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| k | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| * | | * | | k | | k | | s | | * |
| * | | s | | * | | k | | * | | k |
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| k | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| * | | * | | k | | k | | k | | * |
| * | | s | | * | | k | | * | | k |
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| k | | s | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| s | | * | | k | | k | | k | | * |
| * | | s | | * | | k | | * | | k | 
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | k | | k | | * | | s |
| k | | k | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| s | | * | | k | | k | | k | | * |
| * | | s | | * | | k | | * | | k |
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
--------------------------------------------------
| * | | s | | s | | k | | * | | s |
| k | | k | | * | | k | | s | | s |
| s | | * | | s | | * | | k | | s |
| s | | * | | k | | k | | k | | * |
| * | | s | | * | | k | | * | | k |
| s | | * | | k | | s | | k | | k |
--------------------------------------------------
Player A
'''    