tables=[]   #declaring array here as variable name as tables

number_of_tables=int(input("Enter number of tables you need :")) # asking the user how many tables you need 

tables=input("Enter the table numbers with comma (,) :")
tables=tables.split(',')

print("1.Basic\n2.Advance\n3.Both")     # asking the user what type of mode you need 

mode = input("Enter the mode you need :") # entering the mode
mode=mode.lower()   # changeing the mode in lower form
if mode not in "basic" and "advance" and "both":
    print(f"Invalid mode '{mode}' ")
elif mode == "basic": # if user select basic it goes to basic mode
    for table in tables:
        number=int(table)
        starting_range=1
        ending_range=10
        print("Easy numbers")
        for table in range(starting_range,ending_range+1):
            print(f"{number} * {table} = {number*table}")
        print("*"*20)
        
elif mode == "advance": # if user select advance it goes to advance mode
    for table in tables:
        number=int(table)
        starting_range=11
        ending_range=20
        print("Advanced numbers")
        for table in range(starting_range,ending_range+1):
            print(f"{number} * {table} = {number*table}")
        print("*"*20)
        
elif mode == "both":    # if user select both it goes to basic mode after finishing basic mode it goes to advance mode
    for table in tables:
        number=int(table)
        starting_range=1
        ending_range=10
        print("Easy numbers")
        for table in range(starting_range,ending_range+1):
            print(f"{number} * {table} = {number*table}")
        print("*"*20)
        starting_range=11
        ending_range=20
        print("Advanced numbers")
        for table in range(starting_range,ending_range+1):
            print(f"{number} * {table} = {number*table}")
        print("*"*20)