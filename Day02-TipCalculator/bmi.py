weight = float(input("Enter you weight (Kg) : "))
height = float(input("Enter you height (cm) : "))

cmToM = height / 100
sq = cmToM ** 2

bmi = round(weight / sq , 2)

print(f"Your BMI is {bmi}")