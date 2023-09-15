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