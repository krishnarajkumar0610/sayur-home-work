"""
Up to Rs. 3,00,000	                    Nil
Rs. 3.00,000 to Rs. 6,00,000	        5% on income which exceeds Rs. 3,00,000 
Rs. 6,00,000 to Rs. 900,000	Rs.         15,000 + 10% on income more than Rs. 6,00,000
Rs. 9,00,000 to Rs. 12,00,000	        Rs. 45,000 + 15% on income more than Rs. 9,00,000
Rs. 12,00,000 to Rs. 1500,000	        Rs. 90,000 + 20% on income more than Rs. 12,00,000
Above Rs. 15,00,000	                    Rs. 150,000 + 30% on income more than Rs. 15,00,000
"""

salary = int(input("enter your salary : "))
income_slabs = [300000 , 600000 , 900000 , 1200000 , 1500000]
tax_per = [0.05 , 0.10 , 0.15 , 0.20 , 0.3]
tax = 0
tax_sort = 0
for i in range(len(income_slabs)):
        if salary < income_slabs[i]:
            tax = 0
            break
        if i == len(income_slabs) - 1 :
            tax = tax_sort + ((income_slabs[i]-salary)tax_per[i])
            break
        elif income_slabs[i] < salary <= income_slabs[i+1] :
            tax = tax_sort + ((salary - income_slabs[i])tax_per[i])
            break
        else:
            tax_sort += income_slabs[0]*tax_per[i] 
print(tax)

#800000 - 0 + 15000 + 20000 

# salary = int(input())   
# slabs=[300000,600000,900000,1200000,1500000]
# percentage=[0.05,0.1,0.15,0.2,0.3]
# previous_tax=[0,15000,45000,90000,150000]    
# tax=0
# for i in range(0,len(slabs)):
#     if salary<=slabs[i]:
#         tax = previous_tax[i] + (percentage[i] * (salary - slabs[i]))
# print(f"Income tax : {tax}")
# incom_taxes=[300000,600000,900000,1200000,1500000]
# tax_percentage=[0.05,0.10,0.15,0.20,0.30]
# if len(incom_taxes)!=len(tax_percentage):
#     print("Length of charges and incomtax are not equal")
    
# else:
#     salary = int(input("Enter your salary :"))
#     for i in range(0,len(incom_taxes)):
#         if salary<=incom_taxes[i]:
#             print(f"Percentage is {tax_percentage[i]}")
#             break
# taxable_income = int(input("Enter the amount : "))
# slabs = [250000 , 400000,500000 , 1000000]
# tax_per = [0.05 , 0.2 , 0.3]
# cumulative_tax = 0
# for i in range(0,len(slabs)):
#     print("Cummulative Tax is :",cumulative_tax)
#     if taxable_income <= slabs[i]:
#         if i > 0 :
#              tax = cumulative_tax + (taxable_income - slabs[i - 1])*tax_per[i]
#         else :
#             tax = taxable_income * tax_per[i]
#         break
          
#     else:
#         if i > 0 :
#             cumulative_tax = cumulative_tax + (slabs[i] - slabs[i -1]) * tax_per[i]
#         else :
#             cumulative_tax = cumulative_tax + (slabs[i]*tax_per[i])
# print(f"Your tax amount is :{tax}") 
                    
# salary = int(input("Enter your salary : "))
# if salary <= 300000:
#     tax = "nil"

# elif salary> 300000 and salary<=600000:   
#     tax = 0 + (0.05 * (salary - 300000))

# elif salary>600000 and salary<=900000:
#     tax = 15000 + (0.1 * (salary - 600000))

# elif salary>900000 and salary<=1200000:
#     tax = 45000 + (0.15 * (salary - 900000))

# elif salary>1200000 and salary<=1500000:
#     tax = 90000 + (0.2 * (salary - 1200000))

# else:
#     tax = 150000 + (0.3 * (salary - 1500000))