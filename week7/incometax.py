"""
Up to Rs. 3,00,000	                    Nil
Rs. 3.00,000 to Rs. 6,00,000	        5% on income which exceeds Rs. 3,00,000 
Rs. 6,00,000 to Rs. 900,000	Rs.         15,000 + 10% on income more than Rs. 6,00,000
Rs. 9,00,000 to Rs. 12,00,000	        Rs. 45,000 + 15% on income more than Rs. 9,00,000
Rs. 12,00,000 to Rs. 1500,000	        Rs. 90,000 + 20% on income more than Rs. 12,00,000
Above Rs. 15,00,000	                    Rs. 150,000 + 30% on income more than Rs. 15,00,000
"""


salary = int(input("Enter your salary : "))
if salary <= 300000:
    tax = "nil"

elif salary> 300000 and salary<=600000:
    tax = 0.05 * (salary - 300000)

elif salary>600000 and salary<=900000:
    tax = 15000 + (0.1 * (salary - 600000))

elif salary>900000 and salary<=1200000:
    tax = 45000 + (0.15 * (salary - 900000))

elif salary>1200000 and salary<=1500000:
    tax = 90000 + (0.2 * (salary - 1200000))

else:
    tax = 150000 + (0.3 * (salary - 1500000))

print(f"Income tax : {tax}")