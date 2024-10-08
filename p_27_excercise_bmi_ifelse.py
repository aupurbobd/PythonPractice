weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))

bmi=round(weight/height**2,2)
print(bmi)

if bmi<18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi< 25:
    print(f"Your BMI is {bmi} and Your weight is normal.")
else:
    print(f"Your BMI is {bmi} and You are overweight.")