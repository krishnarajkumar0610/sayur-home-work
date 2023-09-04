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
    # while will break when total sales amount is > 10000 or totalbagsSold >10
    choice=input("Enter your choice to buy both bags or green or red :")    # asking user choice   
    choice=choice.lower()   # converting it into lower form
    if choice!="red" and "green" and "both":
        print("Invalid bag color")
        continue   
    if choice =="red" or choice =="both":   # comparing red or both 
        bags=int(input("Enter the number of red bags you need :"))  # asking number of red bags need 
        totalBagsSold=totalBagsSold+bags    # adding the bags count in total bags sold
        count_red+=bags                     # adding the red bags count
        redBags-=bags                       # after buying the red bags decreasing the red bags count
        totalSales=totalSales+(bags*redBags)    # making bill for red bags
        
    if choice =="white" or choice =="both": # comparing green or both
        bags=int(input("Enter the number of green bags you need :"))
        totalBagsSold=totalBagsSold+bags    # adding the bags count in total bags sold
        count_green+=bags                   # adding the green bags count
        greenBags-=bags                     # after buying the green bags decreasing the red bags count
        totalSales=totalSales+(bags*greenBags)  # making bill for green bags    
        
if count_red!=0:
    print(f"{count_red} number of red bags were sold ")
if count_green!=0:
    print(f"{count_green} number of green bags were sold ")
print(f"Total sales {totalSales} and total bags sold {totalBagsSold}") 