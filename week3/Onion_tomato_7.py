'''Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  
Input is the budget.'''

one_kg_onion=20
one_kg_tomato=10.5
budget=int(input("Enter your budget :")) # asking the budget to the user 
onion_kg=int(budget/one_kg_onion)   # this return the number of how many number of kg's can i buy in my budget
tomato_kg=int(budget/one_kg_tomato) # this return the number of how many number of kg's can i buy in my budget

print(f"You can buy {onion_kg} of onions in this budget")   

print(f"You can buy {tomato_kg} of tomatos in this budget")