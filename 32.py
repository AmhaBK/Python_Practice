height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2) 
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "0verweight"
elif bmi < 35:
    category = "Obese"
else:
    category = "Severely obese" 
print("Your BMI is:", bmi)
print("Category:", category)