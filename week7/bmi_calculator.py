def calculate_bmi(weight, height):
    bmi =weight / (height**2)
    return bmi

def weight_message(bmi,age):
    if bmi < 18.5 :
        if age < 20:
            return " You are in Underweight and you should eat foods to gain weight"
        return "Underweight"
    elif bmi >=18.5 and bmi < 24.9:
        if age >=20 and age < 25:
            return " You are in Normalweight and you should drink fruit juice and ent vegetable more"
        return "Normal Weight"
    elif bmi >=25 and bmi < 29.9:
        if age>=25 and age<30:
            "You are in Overweight and you need to do exercise to be fit"
        return "Overweight"
    else:
        return "Obesity"

weight = float(input("Enter your weight : "))   # enter weight 
height = float(input("Enter your height in meters: "))      # enter height 
age=int(input("Enter your age :"))

if(weight and height !=0):  # this is true when we give correct input
    bmi = calculate_bmi(weight, height)  # passing the values in argunments
    message=weight_message(bmi,age) # after getting the bmi value return what message is for our weight
    print(f"Your BMI is: {bmi}")
    print(f"Interpretation: {message}")
else:
    print("Enter valid weight and height to check")