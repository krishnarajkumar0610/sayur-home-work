monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]
base_pay = 10000
previousMonthSalary = 0
cumulative = 0
for month , phoneCount in enumerate(monthlySalesList):
    bonus = 0
    if phoneCount >= 5:
        bonus+=5000
        bonus+=(phoneCount - 5) * 1100
    currentMonthsalary = base_pay
    print(f"This {month+1}'s salary before additional bonus : Rs {currentMonthsalary}")
    currentMonthsalary+=bonus
    if previousMonthSalary > 20000 and phoneCount >=20 :
        currentMonthsalary += 50000
        print(f"This {month+1}'s salary after additional bonus : Rs {currentMonthsalary}")
    else:
        print(f"This  {month+1}'s salary after additional bonus : Rs. {currentMonthsalary}")
    previousMonthSalary = currentMonthsalary
    cumulative +=currentMonthsalary
    print(f"Cumulative amount : {cumulative}")
    if cumulative>=100000:
        base_pay = base_pay*0.05
        cumulative=0