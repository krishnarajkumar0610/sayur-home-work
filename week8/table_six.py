# 6. Same as the above. Ask the user if they want only the basic or only the advanced or both.
# Print what the user is asking. 
# Also ask the user what number table they want to print
# Easy numbers
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30
def basic_mode(table_number):
    starting_range=1
    ending_range=10
    print("Easy numbers")
    for table in range(starting_range,ending_range+1):
        print(f"{table_number} * {table} = {table_number*table}")
    print("********************")
        
def advanced_mode(table_number):
    starting_range=11
    ending_range=20
    print("Advanced numbers")
    for table in range(starting_range,ending_range+1):
        print(f"{table_number} * {table} = {table_number*table}")
    print("********************")
print("1.BASIC\n2.ADVANCED\n3.BOTH")
mode=input("Enter basic or advanced or both :") #asking what method we need 
mode=mode.lower()   # changing it as lower form
table_number=int(input("Enter your table number you need :"))
if(mode in "basic"):
    basic_mode(table_number)
elif(mode in "advanced"):
    advanced_mode(table_number)
elif(mode in "both"):
     basic_mode(table_number)
     advanced_mode(table_number)
else:
     print("Invalid mode")