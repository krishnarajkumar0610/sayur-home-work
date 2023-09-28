# 3. Accept 2 integers. print all nos which are mirror nos falling 
# between the range.
# eg: first no 300
#  second no 400
# 303,313,323.......393


st_num = int(input("Enter the starting range number : "))   # asking the starting  number 
ending_num = int(input("Enter the ending range number : ")) # asking the ending  number 
mirror_numbers=[]
for number in range(st_num,ending_num+1):   # to traverse the numbers
    ans_num=0       # creating one local variable ans assigned 0 
    temp_num=number # creating temp variable and stored the number
    while(temp_num!=0): # traverse into that number
        rem = temp_num % 10 # getting last number from the number
        ans = (ans_num*10)+rem  
        temp_num//=10   # removing the last number from the number
    if number == ans:   # if my original number and answer is correct then it is mirror number
        mirror_numbers.append(number)   # adding in list
    
print(f"Mirror numbers : {mirror_numbers}") 