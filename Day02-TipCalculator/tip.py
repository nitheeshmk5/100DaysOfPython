print("Welcome to Nmk Tip Calculatorrr !!")
totalBill = float(input("Enter the total bill amount : "))
tipPercentage = int(input("Enter the tip percentage (10%,12%,15%) : "))

#Other than 10,12,15
li = [10,12,15]
while tipPercentage not in li:
    print("Enter a vaild tip !!")
    tipPercentage = int(input("Enter the tip percentage (10%,12%,15%) : "))
    
tipCal = totalBill * (tipPercentage / 100)
plusTip = totalBill + tipCal

split = int(input("Enter the number of person to split : "))
eachPerson = round(plusTip / split , 2)


print("+----------------------------------+")
print(f"Each should pay {eachPerson} rs")
print("+----------------------------------+")