'''
Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
 person is half of lunch cost. Cost of the hall is Rs 200 per person.
  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
  Decide what should be the input and calculate the cost.
'''
def calculate_cost(guest):
    lunch_per_person=200
    breakfast_per_person=lunch_per_person/2
    hall_per_person=200
    decoration_per_person=0.5
    parking_per_person=0.1
    
    
    lunch_budget = guest * lunch_per_person       # number of guests multiplied with lunch per person
    
    breakfast_budget = guest * breakfast_per_person  #number of guests multiplied with breakfast_per_person
    
    hall_budget = hall_per_person * guest   #number of guests multiplied with hall_per_person
    
    decoration_budget = guest * decoration_per_person #number of guests multiplied with  decoration_per_person
    
    parking_budget = guest * parking_per_person #number of guests multiplied with parking_per_person
    
    total_budget=lunch_budget+breakfast_budget+hall_budget+decoration_budget+parking_budget
    #addded all budgets and stored in total budget  
    
    return total_budget # returning the total budget

guests=int(input("Enter number of guests are you invited for wedding :")) # number of members invited for wedding
total_budget=0
if guests<1: # if guest is lessthan 1 i want to invite guests
    print("Invite guests to atten the wedding")
else:
    total_budget=calculate_cost(guests)
    print(f"The total wedding hall and others budget is : {total_budget}")