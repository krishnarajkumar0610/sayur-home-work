######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

lines = int(input("Enter number of lines :"))
number=1
while(number<=lines):   # this loops run untill number reaches 10. After reaching 10 and executing the loop it will break the loop
    if input("Enter space to print $ ") == " ": # asking user to click space bar to execute if statement
        print(' '*(lines-number),end='')        # printing  (" " * number of lines - loop variable)
        print(f"{'$ '*number}")     # printing "$ " * loop variable
        number+=1   # increamenting loop variable
    else:
        break




# lines = int(input("Enter number of lines :"))
# number=1
# temp_num=number
# while(lines>temp_num):
#     if number<=5:
#         if input("Enter space to print $ :") == " ":
#             print(' '*(lines - number),end='')
#             print(f"{'$ '*temp_num}")
#             temp_num+=1
#             lines-=1
#         else:
#             break
#     else:
#         number=1