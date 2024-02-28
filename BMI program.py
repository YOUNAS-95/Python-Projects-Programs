weight=float(input("weight:"))
height=float(input("hieght"))
BMI=weight/height
print(BMI)
if BMI<18.5:
    print("Underweight")
elif BMI<24.9:
    print("Normalweight")
elif BMI<29.9:
    print("Overweight")
else:
    print("Obese")
