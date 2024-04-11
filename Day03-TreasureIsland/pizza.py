smallPizza , mediumPizza , largePizza = 0 , 0, 0

print("Welcome to Python Pizza Hut !🍕")
size = input("Enter the size of the pizza : (S - small,M - Medium,L - large) ").upper()
toppings = input("Do you want topping ? (Y or N) ").upper()
cheese = input("Do you want extra cheese ? (Y or N) ").upper()

if size == "S":
    smallPizza = 15
    if toppings == "Y":
        smallPizza += 2
    if cheese == "Y":
        smallPizza += 5
elif size == "M":
    mediumPizza = 20
    if toppings == "Y":
        mediumPizza += 3
    if cheese == "Y":
        mediumPizza += 5
elif size == "L":
    largePizza = 25
    if toppings == "Y":
        largePizza += 3
    if cheese == "Y":
        largePizza += 5

print('+-------------------- PIZZA READY --------------------+')    
print(f"Total bill is ${smallPizza + mediumPizza + largePizza}")


'''
also

bill = 0
if S , bill = 15

can make bill as main variable
'''