########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit

total_costPrize=500
Cafe_Menu=["coffee","tea","greentea","blacktea"]
ordered_list=[]
Cafe_price=[20,15,30,45]
total=0
b=True
while True:
    item=input("Enter your food item :")
    order=""
    b=True
    for i in range(len(Cafe_Menu)):
        if (item==Cafe_Menu[i]):
            quantity = int(input(f"Enter number of {item} you need ? "))
            order=str(quantity)+" "+item+" and it price is "+str(quantity*Cafe_price[i])          
            total=total+(Cafe_price[i]*quantity)
            ordered_list.append(order)
            b=False
            break
    if b:
        print(f"Sorry sir...{item} is not available")
    if int(input("Enter 1 to cancel order or 0 to continue ordeer :")):        
        break
    print()
print(f"Your Ordered list : {ordered_list}")
print(f"Your total bill amount is : {total}")
if total<total_costPrize:
    print(f"You had loss because your total profit = {total} is < total invested amount per day = {total_costPrize}")
elif total>total_costPrize:
    print(f"You had get profit your total profit = {total} is > total invested amount per day = {total_costPrize}")
    
    
''' 
OUTPUT - 1 
------------

Enter your food item :tea
Enter number of tea you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :coffee
Enter number of coffee you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :greentea
Enter number of greentea you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :blacktea
Enter number of blacktea you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :applejuice
Sorry sir...applejuice is not available
Enter 1 to cancel order or 0 to continue ordeer :1
Your Ordered list : ['5 tea and it price is 75', '5 coffee and it price is 100', '5 greentea and it price is 150', '5 blacktea and it price is 225']
Your total bill amount is : 550
You had get profit your total profit = 550 is > total invested amount per day = 500

------------

OUTPUT - 2
----------

Enter your food item :tea
Enter number of tea you need ? 2
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :coffee
Enter number of coffee you need ? 2
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :greentea
Enter number of greentea you need ? 2
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :blacktea
Enter number of blacktea you need ? 2
Enter 1 to cancel order or 0 to continue ordeer :0

Enter your food item :apple juice
Sorry sir...apple juice is not available
Enter 1 to cancel order or 0 to continue ordeer :1
Your Ordered list : ['2 tea and it price is 30', '2 coffee and it price is 40', '2 greentea and it price is 60', '2 blacktea and it price is 90']
Your total bill amount is : 220
You had loss because your total profit = 220 is < total invested amount per day = 500

----------

'''