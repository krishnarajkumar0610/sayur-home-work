# Problem 1
# Wrote a program for seat reservation in a theatre.
# You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
# When the user asks for tickets, you need to provide them tickets in the form of seat no.
# For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
# Print the theatre configuaration at the end of each transaction.

def display(seats):
    row=65
    for outer_loop in seats:
        print(f"Row {chr(row)} : ",end='')
        for inner_loop in outer_loop:
            if inner_loop=='o':
                print(inner_loop,end=' ')
            else:
                print('-',end=' ')
        print()
        row+=1
        
def bookTickets(seats):
    print("-----------------------------------")
    display(seats)
    print("-----------------------------------")
    row = int(input("Enter the row : "))
    seat = int(input("Enter number of seats you need : "))
    row-=1
    if seats[row].count('o')<seat:
        print("Not have maximum seats")
        return
    else:
        booked_slots=[]
        row_index=65
        row_index+=row
        for index in range (len(seats[row])):
            if seat==0:
                break
            if seats[row][index]=='o':
                seats[row][index]='-'
                booked_slots.append(f"{chr(row_index)+str(index+1)}")
                seat-=1 
        print(f"Your booked Slots : {booked_slots}")    
       
seats = [
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
]

while(True):
    print("1.Book Tickets")
    print("2.Close App")
    
    opt = int(input("Enter the option : "))
    
    if opt == 1:
        bookTickets(seats)
    elif opt == 2:
        print("Thank you...",exit(0))
    else:
        print("Enter correct option")
        
        
# output

# 1.Book Tickets
# 2.Close App        
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o 
# Row B : o o o o o
# Row C : o o o o o
# Row D : o o o o o
# Row E : o o o o o
# -----------------------------------
# Enter the row : 1
# Enter number of seats you need : 2
# Your booked Slots : ['A1', 'A2']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : - - o o o
# Row B : o o o o o
# Row C : o o o o o
# Row D : o o o o o
# Row E : o o o o o
# -----------------------------------
# Enter the row : 1
# Enter number of seats you need : 3
# Your booked Slots : ['A3', 'A4', 'A5']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : - - - - -
# Row B : o o o o o
# Row C : o o o o o
# Row D : o o o o o
# Row E : o o o o o
# -----------------------------------
# Enter the row : 1
# Enter number of seats you need : 3
# Not have maximum seats
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# Row A : - - - - -
# PS F:\Sayur learning\sayur-home-work>  f:; cd 'f:\Sayur learning\sayur-home-work'; & 'C:\Users\User-Hp\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\User-Hp\.vscode\extensions\ms-python.python-2023.20.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '63161' '--' 'f:\Sayur learning\sayur-home-work\LT Training\Day 5\Threatre.py' 
# 1.Book Tickets
# 2.Close App        
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o
# Row B : o o o o o
# Row C : o o o o o
# Row D : o o o o o
# Row E : o o o o o
# -----------------------------------
# Enter the row : 4
# Enter number of seats you need : 5
# Your booked Slots : ['D1', 'D2', 'D3', 'D4', 'D5']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o
# Row B : o o o o o
# Row C : o o o o o
# Row D : - - - - -
# Row E : o o o o o
# -----------------------------------
# Enter the row : 4
# Enter number of seats you need : 5
# Not have maximum seats
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o
# Row B : o o o o o
# Row C : o o o o o
# Row D : - - - - -
# Row E : o o o o o
# -----------------------------------
# Enter the row : 2
# Enter number of seats you need : 3
# Your booked Slots : ['B1', 'B2', 'B3']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o
# Row B : - - - o o
# Row C : o o o o o
# Row D : - - - - -
# Row E : o o o o o
# -----------------------------------
# Enter the row : 2
# Enter number of seats you need : 2
# Your booked Slots : ['B4', 'B5']
# 1.Book Tickets
# 2.Close App
# Enter the option : 2