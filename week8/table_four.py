# 4.Print the following
# My Tables
# Table  10
# 10 * 1 = 10
# 10 * 2 = 20
# 10 * 3 = 30
# 10 * 4 = 40
# 10 * 5 = 50
# **********
# Table  8
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# **********
# Table  6
# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# **********
# Table  4
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20
# **********
# Table  2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# **********
# End of tables
starting_table=int(input("Enter your starting table number :"))# asking starting table number
ending_table=int(input("Enter your ending table : "))# asking ending table number 

if ending_table>starting_table:  # if my ending table number is > starting table number it will false 
    print(f"ending table is > starting table")
else:
    table_range=int(input("Enter your table range :"))
    print("My Tables")

    for table in range(starting_table,ending_table,-2): 
        # eg : start with 10 and end with 1 and it will reduced by -2 like:10,8,6,4,2
        num=1 # this num =1 will be set as default as 1 whenever it comes inside outerloop
        print(f"Table {table}")
        for value in range(1,table_range+1):
            print(f"{table} * {num} = {table*num}")
            num+=1
        print("**********")
print("End of tables")