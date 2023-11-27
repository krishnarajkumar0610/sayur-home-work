# Problem 1
# Wrote a program for seat reservation in a theatre.
# You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
# When the user asks for tickets, you need to provide them tickets in the form of seat no.
# For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
# Print the theatre configuaration at the end of each transaction.

def display(seats):
    row=1
    for outer_loop in seats:
        print(f"Row {row} : ",end='')
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
    else:
        for index in range (len(seats[row])):
            if seat==0:
                break
            if seats[row][index]=='o':
                seats[row][index]='-'
                seat-=1 
    


       
    
seats = [
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
    ['o','o','o','o','o'],
]

while(True):
    bookTickets(seats)