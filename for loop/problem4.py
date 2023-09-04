######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.
#      1  2  3  4  5
#   ********************
# 1 |  1  2  3  4  5
# 2 |  2  4  6  8 10
# 3 |  3  6  9 12 15
# 4 |  4  8 12 16 20
# 5 |  5 10 15 20 25

start_table=int(input("Enter the starting table number :"))
end_table=int(input("Enter the ending table number :"))
range_numbers=int(input("Enter the range number :"))
print(" "*end_table,end='')

for table in range(start_table,end_table+1):
    print(f"{table}",end=' ')
print('\n',end="  ")

print("*"*20)

for table_number in range(start_table,end_table+1):    
    print(f"{table_number:1} |",end='')
    for number in range(1,range_numbers+1):
        print(f" {(table_number*number):2}",end='')           
    print()