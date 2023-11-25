# Problem 1
# Print the following pattern
#           1
#          1 1
#         1 2 1
#        1 3 3 1
#       1 4 6 4 1

n = int(input("Enter the number of rows you need : "))
num = int(input("Enter the number to start : "))
prev = []
tot_row = []

for index in range(1,n+1):  # this for loop is to go up to nth row
    print(' '*(n-index),end=' ')
    tot_row.append(num) # appending the value 1 at 1st
    tot_row.extend(prev)    # extending previous value to the list
    for val in tot_row: # printing the elements from the list
        print(val,end=' ')
    print('\t') 
    prev.clear()    # clearing the previous list
    for i in range(len(tot_row)):   # this loop is to append the previous row elements in the previous list
        if i == len(tot_row)-1: # if my i is > list length then it causes index out of bound 
            prev.append(num)
            break
        ans = tot_row[i]+tot_row[i+1] # adding pair elements and storing it in the prev list
        prev.append(ans)    
    tot_row.clear() # clearing the total list 
    
    
# output

# Enter the number of rows you need : 5
# Enter the number to start : 1
#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 
#  1 4 6 4 1 