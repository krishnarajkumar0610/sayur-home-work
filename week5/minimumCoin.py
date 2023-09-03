'''You have three types of coins , values of 1, 3 and 5
given a number, you need to find minimum coins required. 
eg., if input is 8 - answers 5(1), 3(1) - 2 coins 
if input is 10 - answer is 5(2) - 2 coins
if input is 4 - answer is 3(1), 1(1) - 2 coins'''
def count_coins(amount):
    coin_one=1
    coin_three=3
    coin_five=5
    tot_count,count_one,count_three,count_five=0,0,0,0   # initializing all coin count as 0
    while amount!=0:
        if(amount>=5):  # if my amount greaterthan 5 
            amount-=coin_five   # minus 5 from amount
            count_five+=1   # increament coin_five +1
            
        elif(amount>=3 and amount<5):        # if my amount greaterthan equal to 3  and lessthan 5 
            amount-=coin_three      # minus 3 from amount
            count_three+=1          # increament coin_three +1
            
        elif(amount>=1 and amount<3):    # if my amount greaterthan equal to 1  and lessthan 3 
            amount-=coin_one        # minus 1 from amount
            count_one+=1# increament coin_one  +1
            
    total_count=count_one+count_three+count_five     # adding all coin counts and stored in total_count
    print(f"Number of one's:{count_one}")
    print(f"Number of three's:{count_three}")
    print(f"Number of five's:{count_five}")
    print(f"Total coins :{total_count} ")
amount=int(input("Enter the amount :"))
count_coins(amount)
