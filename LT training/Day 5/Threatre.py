# Problem 1
# Wrote a program for seat reservation in a theatre.
# You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
# When the user asks for tickets, you need to provide them tickets in the form of seat no.
# For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
# Print the theatre configuaration at the end of each transaction.

def display(seats): # this is to display the theatre seats
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
    rows=['A','B','C','D','E']  # this list contains the rows of the seats
    print("-----------------------------------")
    display(seats)  # displaying the seats to the customer
    print("-----------------------------------")
    try:    
        row = int(rows.index(input("Enter the row : ").upper()))
        # in this changing the input to finding the index and storing in the variable
    except Exception:   # if i give number or any invalid row character
            print("Enter valid row")        
            return  
    seat = int(input("Enter number of seats you need : "))  # asking number of seats
    if seats[row].count('o')<seat : # if seats are > available seats
        print("Not have maximum seats")
        return
    elif seat<=0:   # if seats are invalid number 
        print("Enter valid seat numbers")
        return
    else:   
        booked_slots=[] # to store the booked seats
        row_index=65
        row_index+=row
        for index in range (len(seats[row])):
            if seat==0:
                break
            if seats[row][index]=='o':  # if seats are not booked then booking it
                seats[row][index]='-'       # as -
                booked_slots.append(f"{chr(row_index)+str(index+1)}")   # adding the booking seats in the list
                seat-=1 
        print(f"Your booked Slots : {booked_slots}")  # printing the booked slots  
        
       
seats = [
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],  # initializing seats in theatre
    ['o','o','o','o','o'],
    ['o','o','o','o','o']
]

while(True):    # this loop will continuously run until i stop my booking 
    print("1.Book Tickets")
    print("2.Close App")
    
    opt = int(input("Enter the option : ")) 

    if opt == 1:    # if the option is 1 then book my tickets
        bookTickets(seats)  # calling booking fuction
        
    elif opt == 2:      # if the option is 2 then closing the app
        print("Thank you...Available seats are \n")
        display(seats)  # then displaying the available seats alone
        print(exit(0))
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
# Enter the row : 3
# Enter valid row
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
# Enter the row : c
# Enter number of seats you need : 3
# Your booked Slots : ['C1', 'C2', 'C3']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o
# Row B : o o o o o
# Row C : - - - o o
# Row D : o o o o o
# Row E : o o o o o
# -----------------------------------
# Enter the row : e
# Enter number of seats you need : 1
# Your booked Slots : ['E1']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : o o o o o
# Row B : o o o o o
# Row C : - - - o o
# Row D : o o o o o
# Row E : - o o o o
# -----------------------------------
# Enter the row : a
# Enter number of seats you need : 4
# Your booked Slots : ['A1', 'A2', 'A3', 'A4']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : - - - - o
# Row B : o o o o o
# Row C : - - - o o
# Row D : o o o o o
# Row E : - o o o o
# -----------------------------------
# Enter the row : s
# Enter valid row
# 1.Book Tickets
# 2.Close App
# Enter the option : 4
# Enter correct option
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : - - - - o
# Row B : o o o o o
# Row C : - - - o o
# Row D : o o o o o
# Row E : - o o o o
# -----------------------------------
# Enter the row : d
# Enter number of seats you need : 4
# Your booked Slots : ['D1', 'D2', 'D3', 'D4']
# 1.Book Tickets
# 2.Close App
# Enter the option : 1
# -----------------------------------
# Row A : - - - - o
# Row B : o o o o o
# Row C : - - - o o
# Row D : - - - - o
# Row E : - o o o o
# -----------------------------------
# Enter the row : b
# Enter number of seats you need : 2
# Your booked Slots : ['B1', 'B2']
# 1.Book Tickets
# 2.Close App
# Enter the option : 2
# Thank you...Available seats are 

# Row A : - - - - o
# Row B : - - o o o
# Row C : - - - o o
# Row D : - - - - o
# Row E : - o o o o