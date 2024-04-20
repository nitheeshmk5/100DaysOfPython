MENU = [
    {
        'name': 'tea',
        'product_name': 'special tea',
        'ingredients': {
            'water': 2,
            'powder': 0.5
        },
        'cost': 10
    },
    {
        'name': 'gt',
        'product_name': 'Ginger tea',
        'ingredients': {
            'water': 2,
            'powder': 0.4,
            'ginger': '1/4'
        },
        'cost': 15
    },
    {
        'name': 'mt',
        'product_name': 'Masala tea',
        'ingredients': {
            'water': 2,
            'powder': 0.5,
            'ginger': "1/4",
            'mint': "1/2"
        },
        'cost': 20
    }
]

order = input("Enter the order (tea , mt for masala tea , gt for ginger tea) :  ")
amt = 0
details = {}

for i in MENU:
    if i['name'] == order:
        details = i['ingredients']
        amt = i['cost']

print(f"Your order's ingredients : ")
print(details)
print(f"Total bill is {amt}")

giving_amt = float(input("Pay the bill with your amt : "))

while giving_amt < amt:
    print(f"Bill amt is {amt}")
    giving_amt = float(input("Pay the bill with your amt : "))

if giving_amt > amt:
    print(f"Balance amt is {giving_amt - amt}")
    print("Thanks for coming")
else:
    print("Thanks for coming")

