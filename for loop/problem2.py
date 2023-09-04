
######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.
starting_table=int(input("Enter your starting multiplication tables you need :")) # asking number of tables
ending_table=int(input("Enter your ending multiplication tables you need :")) 
number_range=int(input("Enter ending range:")) # asking table range eg : 5 means 1 to 5

for table in range(starting_table,ending_table+1):  # this outer loop for starting with 1 table and ends with table_number
    
    num=1  # this num =1 will be set as default as 1 whenever it comes inside outerloop
    print(f"Table number {table}")
    
    for value in range(1,number_range+1):        
        print(f"{table} * {num} = {table*num}")   # table_number multiplied with number is answer
        num+=1  # incrementing +1 every time in innerloop
    print("*"*20)