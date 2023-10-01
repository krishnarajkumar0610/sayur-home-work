# 3. Accept 2 integers. print all nos which are mirror nos falling 
# between the range.
# eg: first no 300
#  second no 400
# 303,313,323.......393


# Type 1

def find_numbers(st_num,ending_num):
    mirror_numbers=[]   # creating empty list

    for number in range(st_num,ending_num+1):   # to traverse the numbers
        ans_num=0      # creating one local variable ans assigned 0 
        temp_num=number # creating temp variable and stored the number
        while(temp_num!=0): # traverse into that number
            rem = temp_num % 10 # getting last number from the number
            ans_num = (ans_num*10)+rem  
            temp_num//=10   # removing the last number from the number
        if number == ans_num:   # if my original number and answer is correct then it is mirror number
            mirror_numbers.append(number)   # adding in list
    
        ans_num=0 # again assigning as 0 to check next number
    
    return f"Mirror numbers : {mirror_numbers}"


st_num = int(input("Enter the starting range number : "))   # asking the starting  number 
ending_num = int(input("Enter the ending range number : ")) # asking the ending  number 

print(f"Mirror numbers are : {find_numbers(st_num,ending_num)}")

# OUTPUT 1

# Enter the starting range number : 300
# Enter the ending range number : 400
# Mirror numbers : [303, 313, 323, 333, 343, 353, 363, 373, 383, 393]


# Type 2

def find_numbers(st_num,ending_num):
    mirror_numbers=[]   # creating empty list

    for number in range(st_num,ending_num+1):   # to traverse the numbers
        temp_num=str(number)
        number=str(number)
        number=number[::-1]
        if temp_num == number:
            mirror_numbers.append(int(temp_num))
    return mirror_numbers    

st_num = int(input("Enter the starting range number : "))   # asking the starting  number 
ending_num = int(input("Enter the ending range number : ")) # asking the ending  number 

print(f"Mirror numbers are : {find_numbers(st_num,ending_num)}")


# OUTPUT 2

# Enter the starting range number : 300
# Enter the ending range number : 400
# Mirror numbers : [303, 313, 323, 333, 343, 353, 363, 373, 383, 393]