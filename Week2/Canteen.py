'''
The user just bought a few things in your  shop. Ask the user what he bought.
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype
'''

def calculate(vadai_snack,soda_snack,sandwich_snack):
    vadai_price=30 # one vadai price is 30
    
    soda_price=20  # one soda price is 20
    
    sandwich_price=100 # one sandwich price is 100
    
    # total amount stored in bill
    
    bill=float(vadai_snack*vadai_price)+(soda_snack*soda_price)+(sandwich_snack*sandwich_price)  
    
    print(f"Your bill amount is : {bill}")
    
    amount=float(input("Pay the bill amount :")) # asking customer to pay bill
    
    if amount>bill: # if customer pay more than bill amount we need to return balance amount
        return f"Bill has been paid and balance amount is {amount-bill}"
    
    elif amount==bill: # if they pay correct amount the bill has paid
        return "Bill has paid"
    
    return f"Insufficient amount pay more rupees {bill-amount}"  # if they pay less then bill amount thats not enough

# asking user how many vadai,soda,sandwich they bought

vadai_snack=int(input("Enter number of vadai you bought :"))  

soda_snack=int(input("Enter number of soda you bought :"))    

sandwich_snack=int(input("Enter number of sandwich you bougth :")) 

print(calculate(vadai_snack,soda_snack,sandwich_snack))