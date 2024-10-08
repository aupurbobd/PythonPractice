#BMI calculation
height = float(input("Enter your height in meter:"))
weight = int(input("Enter your weight in KGs:"))
bmi=round(weight/(height ** 2))
print("Your Body Mass Index (BMI) is "+ str(bmi))
