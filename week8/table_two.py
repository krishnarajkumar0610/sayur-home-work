# 2. Print the following using two for loops

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15

table_number=int(input("Enter your number of multiplication tables you need :")) # asking number of tables
number_range=int(input("Enter ending range:")) # asking table range eg : 5 means 1 to 5

for table in range(1,table_number+1):  # this outer loop for starting with 1 table and ends with table_number
    
    num=1  # this num =1 will be set as default as 1 whenever it comes inside outerloop
    
    for value in range(1,number_range+1):
        
        print(f"{table} * {num} = {table*num}")   # table_number multiplied with number is answer
        
        num+=1  # incrementing +1 every time in innerloop
        