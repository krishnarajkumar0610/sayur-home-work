########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 green bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, greenBags = 100, 200
totalSales , totalBagsSold = 0,0
bags=0
count_red,count_green=0,0

while ( totalBagsSold <10 and totalSales < 10000) :
    #Ask customer for input
    choice=input("Enter your choice to buy both bags or green or red :")
    choice=choice.lower()
    if choice =="red" or choice =="both":
        bags=int(input("Enter the number of red bags you need :"))
        totalBagsSold=totalBagsSold+bags
        count_red+=bags
        redBags-=bags
        totalSales=totalSales+(bags*redBags)
    if choice =="white" or choice =="both":
        bags=int(input("Enter the number of green bags you need :"))
        totalBagsSold=totalBagsSold+bags
        count_green+=bags
        greenBags-=bags
        totalSales=totalSales+(bags*greenBags)
if count_red!=0:
    print(f"{count_red} number of red bags were sold ")
if count_green!=0:
    print(f"{count_green} number of green bags were sold ")
print(f"Total sales {totalSales} and total bags sold {totalBagsSold}") 