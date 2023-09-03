'''
7.Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  
Input is the budget. 
7.1 Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.
7.2 Same as above, but add 3% of the budget for petrol expenses.


def calculate_kilogram(budget,city):
    temp_budget=budget
    onion_kg,tomato_kg=0,0
    total,balance=0,0
    one_kg_onion=20
    one_kg_tomato=10.5
    pertrol_expenses=0.03
    
    if city=="Madurai":
        # while coming to madurai we need to put petrol so i have put petrol so amount is reduced
        budget=budget-pertrol_expenses
        print(f"You came to {city} so you put petrol now your current balance amount is :{budget}")
        
         # in madurai 1kg of onion is 34 rupees
        one_kg_onion=34
            
        # if my budget can buy more than 1kg of onion then i can buy more kg's of onions
        if int(budget/one_kg_onion)>=1: 
            onion_kg=int(budget/one_kg_onion)
            balance=budget-(onion_kg*one_kg_onion) 
            
            # if my balance amount is eligible to buy atleast 1kg of tomatos i can buy tomatos also
            
            if balance > one_kg_tomato:
                tomato_kg=balance/one_kg_tomato
                balance=balance-(tomato_kg*one_kg_tomato)
                print(f"You can buy {onion_kg} kg's of onions and your balance is {balance}")
                balance=balance-(tomato_kg*one_kg_tomato)
                print(f"After buying tomatos now your current balance is {balance}")
            else:
                print(f"You can buy only {onion_kg} kg's of onions and your balance is {balance}")
                
         # if my budget is not capable for buying tomatos my money is not enough so else block will work       
        else:
            print("Insufficient amount to buy vegetables")
            
            
    elif city=="Chennai":
        # while coming to chennai we need to put petrol so i have put petrol so amount is reduced
        budget=budget-pertrol_expenses
        print(f"You came to {city} so you put petrol now your current balance amount is :{budget}")
        
        # in madurai 1kg of onion is 30 rupees
        one_kg_onion=30
            
            
        # if my budget can buy more than 1kg of onion then i can buy more kg's of onions
        if int(budget/one_kg_onion)>=1:            
            onion_kg=int(budget/one_kg_onion)
            balance=budget-(onion_kg*one_kg_onion)
            
            # if my balance amount is eligible to buy atleast 1kg of tomatos i can buy tomatos also
            if balance > one_kg_tomato:
                tomato_kg=balance/one_kg_tomato                
                print(f"You can buy {onion_kg} kg's of onions and your balance is {balance} and you can buy {tomato_kg} kg's of tomatos ")
                balance=balance-(tomato_kg*one_kg_tomato)
                print(f"After buying tomatos now your current balance is {balance}")
            
            else:
                print(f"You can buy only {onion_kg} kg's of onions and your balance is {balance}")
        else:
            print("Insufficient amount to buy vegetables")
            
            
    elif city=="Trichy":
        budget=budget-pertrol_expenses
        print(f"You came to {city} so you put petrol now your current balance amount is :{budget}")
        one_kg_onion=27
        if int(budget/one_kg_onion)>=1:            
            onion_kg=int(budget/one_kg_onion)
            balance=budget-(onion_kg*one_kg_onion)
            if balance > one_kg_tomato:
                tomato_kg=balance/one_kg_tomato                
                print(f"You can buy {onion_kg} kg's of onions and your balance is {balance} and you can buy {tomato_kg} kg's of tomatos ")
                balance=balance-(tomato_kg*one_kg_tomato)
                print(f"After buying tomatos now your current balance is {balance}")
            
            else:
                print(f"You can buy only {onion_kg} kg's of onions and your balance is {balance}")
        else:
            print("Insufficient amount to buy vegetables")       
    else:
        print("Invalid city")
        
        
budget=float(input("Enter your buget  :"))
city=input("Enter the city Madurai or Chennai or Trichy :")
if budget<10:
    print("Insufficient amount to buy vegetables")
else:
    calculate_kilogram(budget,city)'''