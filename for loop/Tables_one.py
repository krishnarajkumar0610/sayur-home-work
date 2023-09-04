# 1. Print the following using for loop
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
table_number=int(input("Enter the table number you want :"))   # asking table number

table_range=int(input("Enter your table range :"))          # asking table range eg : 5 means 1 to 5

for number in range(1,table_range+1):   # this is starts with 1 and ends with table_range eg : 1 to 5
    
    print(f"{table_number} * {number} = {table_number*number}")     # table_number multiplied with number is answer
    