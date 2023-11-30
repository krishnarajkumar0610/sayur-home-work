def display(seats):
    row = 65
    for outer_loop in seats:
        print(f"Row {chr(row)}: ", end='')
        for inner_loop in outer_loop:
            if inner_loop == 'o':
                print(inner_loop, end=' ')
            else:
                print('-', end=' ')
        print()
        row += 1


def calculate_ticket_price(row):
    if row <= 3:
        return 100
    elif 4 <= row <= 5:
        return 200
    else:
        return 300


def book_tickets(seats):
    rows = ['A', 'B', 'C', 'D', 'E','F','G','H']
    print("-----------------------------------")
    display(seats)
    print("-----------------------------------")
    try:
        row_input = input("Enter the row (A-E): ").upper()
        row = int(rows.index(row_input))
    except Exception:
        print("Enter a valid row (A-E)")
        return

    seat = int(input("Enter the number of seats you need: "))

    if seats[row].count('o') < seat:
        print("Not enough available seats")
        return
    elif seat <= 0:
        print("Enter a valid number of seats")
        return
    else:
        booked_slots = []
        total_price=0
        row_index = 65
        row_index += row
        for index in range(len(seats[row])):
            if seat == 0:
                break
            if seats[row][index] == 'o':
                price = calculate_ticket_price(row + 1)
                if index == 0 or index == len(seats[row]) - 1:
                    price -= 50  # Discount for seats close to the wall
                seats[row][index] = '-'
                booked_slots.append(f"{chr(row_index) + str(index + 1)} (Rs {price})")
                total_price+=price
                seat -= 1
        
        print(f"Your booked Slots: {booked_slots}")
        print(f"Total Price: Rs {total_price}")


seats = [
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o'],
    ['o', 'o', 'o', 'o', 'o']
]

while True:
    print("1. Book Tickets")
    print("2. Close App")

    opt = int(input("Enter the option: "))

    if opt == 1:
        book_tickets(seats)
    elif opt == 2:
        print("Thank you. Available seats are \n")
        display(seats)
        exit(0)
    else:
        print("Enter the correct option")


# output 

# 1. Book Tickets
# 2. Close App
# Enter the option: 1
# -----------------------------------
# Row A: o o o o o
# Row B: o o o o o
# Row C: o o o o o
# Row D: o o o o o
# Row E: o o o o o
# Row F: o o o o o
# Row G: o o o o o
# Row H: o o o o o
# -----------------------------------
# Enter the row (A-E): h
# Enter the number of seats you need: 5
# Your booked Slots: ['H1 (Rs 250)', 'H2 (Rs 300)', 'H3 (Rs 300)', 'H4 (Rs 300)', 'H5 (Rs 250)']
# Total Price: Rs 1400
# 1. Book Tickets
# 2. Close App
# Enter the option: 1
# -----------------------------------
# Row A: o o o o o
# Row B: o o o o o
# Row C: o o o o o
# Row D: o o o o o
# Row E: o o o o o
# Row F: o o o o o
# Row G: o o o o o 
# Row H: - - - - -
# -----------------------------------
# Enter the row (A-E): a
# Enter the number of seats you need: 3
# Your booked Slots: ['A1 (Rs 50)', 'A2 (Rs 100)', 'A3 (Rs 100)']
# Total Price: Rs 250
# 1. Book Tickets
# 2. Close App
# Enter the option: 1
# -----------------------------------
# Row A: - - - o o
# Row B: o o o o o
# Row C: o o o o o
# Row D: o o o o o
# Row E: o o o o o
# Row F: o o o o o
# Row G: o o o o o
# Row H: - - - - -
# -----------------------------------
# Enter the row (A-E): d
# Enter the number of seats you need: 2
# Your booked Slots: ['D1 (Rs 150)', 'D2 (Rs 200)']
# Total Price: Rs 350
# 1. Book Tickets
# 2. Close App
# Enter the option: 2
# Thank you. Available seats are 

# Row A: - - - o o
# Row B: o o o o o
# Row C: o o o o o
# Row D: - - o o o
# Row E: o o o o o
# Row F: o o o o o
# Row G: o o o o o
# Row H: - - - - -