'''Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided.'''

        
number = int(input("Enter the number :"))
if number<3:
    print("Its already lessthan 3")
else:
    count=0
    while number>=3:  # i used while loop for i dont know when my number becomes < 3
        number=int(number/3)
        count=count+1
        if number<3:
            print(f"Now number is lessthan 3 : {number}")
        else:
            print(f"number {number}")
print(f"Total number of times is : {count}")