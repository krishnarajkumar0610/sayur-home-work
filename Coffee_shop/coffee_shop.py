########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit

total_costPrize=500
Cafe_Menu=["coffee","tea","greentea","blacktea"]
ordered_list={}
Cafe_price=[20,15,30,45]
total=0
while True:
    item=input("Enter your food item :")
    for i in range(len(Cafe_Menu)):
        if (item==Cafe_Menu[i]):
            quantity = int(input(f"Enter number of items {item} you need ? "))
            total=total+(Cafe_price[i]*quantity)
            ordered_list[item]=quantity
            break
    if int(input("Enter 1 to cancel order or 0 to continue ordeer :")):
        break
print(f"Your Ordered list : {ordered_list}")
print(f"Your total bill amount is : {total}")
if total<total_costPrize:
    print(f"You had lost because your total profit = {total} is < total cost price = {total_costPrize}")
elif total>total_costPrize:
    print(f"You had get profit your total profit = {total} is > total cost price = {total_costPrize}")
    
    
''' 
OUTPUT - 1 
------------

Enter your food item :coffee
Enter number of items coffee you need ? 3
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :tea
Enter number of items tea you need ? 3
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :greentea
Enter number of items greentea you need ? 3
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :blacktea
Enter number of items blacktea you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :tea
Enter number of items tea you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :1
Your Ordered list : {'coffee': 3, 'tea': 5, 'greentea': 3, 'blacktea': 5}
Your total bill amount is : 495
You had lost because your total profit = 495 is < total cost price = 500

------------

OUTPUT - 2
----------

Enter your food item :coffee
Enter number of items coffee you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :tea
Enter number of items tea you need ? 5
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :greentea
Enter number of items greentea you need ? 8
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :blacktea
Enter number of items blacktea you need ? 6
Enter 1 to cancel order or 0 to continue ordeer :0
Enter your food item :tea
Enter number of items tea you need ? 4
Enter 1 to cancel order or 0 to continue ordeer :1
Your Ordered list : {'coffee': 5, 'tea': 4, 'greentea': 8, 'blacktea': 6}
Your total bill amount is : 745
You had get profit your total profit = 745 is > total cost price = 500 

----------

'''