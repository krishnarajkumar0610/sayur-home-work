'''7.2 Same as above, but add 3% of the budget for petrol expenses.'''
def calculate_kilograms(budget,city):
    # same as previous program all comands are similar to this program but in this only we added petrol expenses
    onion_kg=0
    if city=="Madurai":
        one_kg_onion=34
        onion_kg=int(budget/one_kg_onion)
        if onion_kg<1:
            return f"You can't buy onions in this budget in {city}"
        return f"You can buy {onion_kg} of onions in this budget in {city}"
    elif city=="Chennai":
        one_kg_onion=30
        onion_kg=int(budget/one_kg_tomato)
        if onion_kg<1:
            return f"You can't buy onions in this budget in {city}"
        return f"You can buy {onion_kg} of onions in this budget in {city}"
    elif city=="Trichy":
        one_kg_onion=27
        onion_kg=int(budget/one_kg_onion)
        if onion_kg<1:
            return f"You can't buy onions in this budget in {city}"
        return f"You can buy {onion_kg} of onions in this budget in {city}"
    else:
        return "Invalid city name"
    
one_kg_tomato=10.5 

tomato_kg,onion_kg=0,0  

petrol_expenses=0.03 
budget=float(input("Enter your budget :"))
city=input("Enter the city :")
budget=budget-petrol_expenses   # here i am putting petrol and going to the particula city so my buget - 0.03
tomato_kg=int(budget/one_kg_tomato)
if tomato_kg==0:
    print(f"You can't buy vegetables because your budget is {budget}")
else:
    onion_kg=calculate_kilograms(budget,city)
    if onion_kg!="Invalid city name":
        print(f"You can buy {tomato_kg} kg's of tomatos and {onion_kg}")
    else:
        print("Invalid city name")