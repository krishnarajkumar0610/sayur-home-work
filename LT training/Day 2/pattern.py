# Problem 1
# Print the following pattern
#           1
#          212   
#         32123
#        4321234
#       543212345

previous=''  # creating this variable to store the previous row numbers
n = int(input("Enter number of rows you need : "))  # asking the input for number of rows
temp=n-1
for index in range(1,n+1):  # this for loop is to run 5 times
    # print(' '*temp,end='')
    temp-=1
    tot_str=str(index)+previous # adding the current index + previous row as string
    print(tot_str)  # printing the total String
    previous=tot_str+str(index+1)    
    # then assigning the total string to previous variable to print with current row and adding the next index position to it
    
    
# output

# Enter number of rows you need : 5
# 1        
# 212      
# 32123    
# 4321234  
# 543212345