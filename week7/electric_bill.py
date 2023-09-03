'''If the consumer’s consumption is less than 500 units means, 
they has to pay zero charges for the first 100 units, 
₹2.25 for the next 100 unit such as consumption between 101 to 200, 
₹4.5 for the units between 200 to 400 and ₹6 per unit for the consumption between 400 to 500 units.

Power Range	 for below 500 Per unit(₹)
0 to 100 is dont need to pay
101-200	 pay Rs:2.25  per unit
201-400	 pay Rs:4.5   per unit
401-500	pay Rs:6.00   per unit

Power Range	 for above 500 Per unit(₹)
0 to 100 is dont need to pay
101-400	 pay Rs:4.50  per unit
401-500	 pay Rs:6.00   per unit
501-600	pay Rs:8.00   per unit
601-800	pay Rs:9.00   per unit
801-1000	pay Rs:10.00   per unit'''

def below_fiveHundren(unit):
    slab1=100
    slab2=200
    slab3=400
    slab4=500
    bill=0
    free_unit=slab1
    if  unit<=100:
        print("You don't need to pay any charges")
        print(exit(0))
        
    elif unit>slab1 and unit<=slab2:
        charges_per_unit=2.25
        print("Energy charges after Govt's subsidy and your unit is in between 101 to 200")     
        unit=unit-free_unit  
        bill=unit*(charges_per_unit)
        
    elif unit>slab2 and unit<=slab3:
        charges_per_unit=4.50
        unit=unit-free_unit
        bill=(100 * 2.25)+((unit-100)*charges_per_unit)
        
    elif unit>slab3 and unit<=slab4:
        charges_per_unit=6.00
        unit=unit-free_unit
        bill=(100*2.25)+(100*4.50)+((unit-200)*charges_per_unit)
        
    return bill  # returning the bill
        
def above_fiveHundred(unit):
    slabs=[100,400,500,600,800,1000]
    charges=[4.50,6.00,8.00,9.00,10.0]
    bill,free_unit=0,100
    if  unit<=slabs[0]:
        print("You don't need to pay any charges")
        print(exit(0))
        
    elif unit>slabs[0] and unit<=slabs[1]:
        charges_per_unit=charges[0]
        unit=unit-free_unit
        bill=unit*charges_per_unit
        
    elif unit>slabs[1] and unit<=slabs[2]:
        charges_per_unit=charges[1]
        unit=unit-free_unit
        bill=(100*charges[0])+((unit-100)*charges_per_unit)
        
    elif unit>slabs[2] and unit<=slabs[3]:  
        charges_per_unit=charges[2]
        unit=unit-free_unit
        bill=(100*charges[0])+(100*charges[1])+((unit-200)*charges_per_unit)
        
    elif unit>slabs[3] and unit<=slabs[4]:
        charges_per_unit=charges[3]
        unit=unit-free_unit
        bill=(100*charges[0])+(100*charges[1])+(100*charges[2])+((unit-300)*charges_per_unit)
        
    elif unit>slabs[4] and unit<=slabs[5]:
        charges_per_unit=charges[4]
        unit=unit-free_unit 
        bill=(100*charges[0])+(100*charges[1])+(100*charges[2])+(100*charges[3])+((unit-400)*charges_per_unit)
        
    return bill # returning the bill

print("Online TNEB Monthly Bill Calculator - 2023 to 2024 ")
name = input("Enter your name :")
unit = int(input("Enter your unit :"))
bill=0
if unit>0 and unit<=500:
    bill=below_fiveHundren(unit)  # this is for <=500
elif unit>500:
    bill=above_fiveHundred(unit)  # this is for > 500
else:
    print(f"Invalid unit {unit}") # unit is < 0 invalit unit
print(f"Your units {unit} and total bill amount is : {bill}")