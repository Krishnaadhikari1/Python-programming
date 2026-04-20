#write a program to calculate BMI 
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
