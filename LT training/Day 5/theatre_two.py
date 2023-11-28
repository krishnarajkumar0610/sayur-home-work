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


def calculate_ticket_price(row, seat, total_rows):
    if row <= 3:
        return 100
    elif 4 <= row <= 12:
        return 200
    else:
        return 300


def book_tickets(seats):
    rows = ['A', 'B', 'C', 'D', 'E']
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
        row_index = 65
        row_index += row
        for index in range(len(seats[row])):
            if seat == 0:
                break
            if seats[row][index] == 'o':
                price = calculate_ticket_price(row + 1, index + 1, len(seats))
                if index == 0 or index == len(seats[row]) - 1:
                    price -= 50  # Discount for seats close to the wall
                seats[row][index] = '-'
                booked_slots.append(f"{chr(row_index) + str(index + 1)} (Rs {price})")
                seat -= 1

        total_price = sum(calculate_ticket_price(row + 1, i + 1, len(seats)) for i in range(len(seats[row])))
        print(f"Your booked Slots: {booked_slots}")
        print(f"Total Price: Rs {total_price}")


seats = [
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
