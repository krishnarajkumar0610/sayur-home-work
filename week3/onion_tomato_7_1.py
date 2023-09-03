'''7.1 Same as above, but the price of Onion is different based on the city. 
Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.'''

def calculate_kilograms(budget,city):  
    onion_kg=0
    if  city=="madurai" :  
        one_kg_onion=34    
        onion_kg=int(budget/one_kg_onion)
        
        if onion_kg<1:    
            return f"You can't buy onions in this budget in {city}" 
        return f"You can buy {onion_kg} of onions in this budget in {city}"  
    
    elif city=="chennai":
        one_kg_onion=30   
        onion_kg=int(budget/one_kg_tomato)
        if onion_kg<1:
             return f"You can't buy onions in this budget in {city}" 
        return f"You can buy {onion_kg} of onions in this budget in {city}"
    
    elif city=="trichy":
        one_kg_onion=27    
        onion_kg=int(budget/one_kg_onion)  
        if onion_kg<1:
            return f"You can't buy onions in this budget in {city}"
        return f"You can buy {onion_kg} of onions in this budget in {city}"
    
    else:
        return "Invalid city name"

one_kg_tomato=10.5   
tomato_kg=0
onion_kg=0
budget=float(input("Enter your budget :"))   # asking budget to the user 
city=input("Enter the city :")   # asking city to buy vegetables
city=city.lower()
tomato_kg=int(budget/one_kg_tomato)      

if tomato_kg==0:   
    print(f"You can't buy vegetables because your budget is {budget}")
    
else:  
    onion_kg=calculate_kilograms(budget,city)   
    if onion_kg!="Invalid city name":
            print(f"You can buy {tomato_kg} kg's of tomatos and {onion_kg}")            
    else:
        print("Invalid city name")