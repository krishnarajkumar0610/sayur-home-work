'''Start with the above. The total cost is split equally by bride and groom.
 Bride has saved Rs50000. Determine if the bride has to take a loan or not. 
 If loan, how much?'''
 
def calculate_cost(guest):
    lunch_per_person=200
    breakfast_per_person=lunch_per_person/2
    hall_per_person=200
    decoration_per_person=0.5
    parking_per_person=0.1
     
    lunch_budget = guest * lunch_per_person   # number of guests multiplied with lunch per person
    
    breakfast_budget = guest * breakfast_per_person #number of guests multiplied with breakfast_per_person
    
    hall_budget = hall_per_person * guest #number of guests multiplied with hall_per_person
    
    decoration_budget = guest * decoration_per_person #number of guests multiplied with  decoration_per_person
    
    parking_budget = guest * parking_per_person #number of guests multiplied with parking_per_person
    
    total_budget=lunch_budget+breakfast_budget+hall_budget+decoration_budget+parking_budget
     # adding all budgets and stored in total
     
    return total_budget   # returning the total amount

def loan(total_budget,bride):
    
    bride_cost=int(total_budget/2) # half amount bride and grrom has to pay so we need to get 1st half for bride
    
    if bride_cost>bride:  # if half amount is greater than bride amount he wants to take loan 
        print("Want to take loan ")
        loan_amount=bride_cost-bride
        print(f"Loan amount is : {loan_amount}")
    else:
        print(f"Bride don't need to take loan he have enough money :{bride}")
        
guests=int(input("Enter number of guests are you invited for wedding :")) 
total_budget=0
if guests<1:
    print("Invite guests to atten the wedding")
else:
    total_budget=calculate_cost(guests)
    print(f"The total wedding hall and others budget is : {total_budget}")
    
bride=50000  
           
loan(total_budget,bride)