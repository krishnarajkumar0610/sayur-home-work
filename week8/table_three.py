# 3. Print the following. Learn how to use print with formatting
# Learn how to print ********* using formatted print
# My Tables
# Table  1
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# **********
# Table  2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# **********
# Table  3
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# **********
# End of tables
table_number=int(input("Enter number of multioplication tables you need :")) # asking number of tables
table_range=int(input("Enter your table range :")) # asking range eg : 5 means 1 to 5
print("My tables\n")
for table in range(1,table_number+1):  # starts with 1 table and ends with table_number what we given eg: 1 to 5
    num=1  # this num =1 will be set as default as 1 whenever it comes inside outerloop
    print(f"------- TABLE {table} -------")     # print the table number whenever it comes inside outerloop
    
    for value in range(1,table_range+1):    # range starts with 1 and ends with what range we given eg : 1 to 5
        print(f"{table} * {num} = {num*table}" )
        num+=1  # incrementing +1 every time in innerloop
    print()     # leaving space everytime when innerloop is finished
print("End of my table") # printing this line when outerloop is finished