weight = float(input("Enter you weight (Kg) : "))
height = float(input("Enter you height (cm) : "))

cmToM = height / 100
sq = cmToM ** 2

bmi = round(weight / sq , 2)

print(f"Your BMI is {bmi}")
if bmi < 18.5: print("Under weight")
elif bmi < 25 : print("Bayapudaathaa , Its Normal !!")
elif bmi < 30 : print("Slightly overweight !")
elif bmi < 35 : print("Over weight !?")
else : print("Cretical obesee ??")