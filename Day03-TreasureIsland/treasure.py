import pyfiglet

T = "Welcome to Treasure Hunt"
diagram = pyfiglet.figlet_format(T)

print(diagram)
print()

print("Welcome to Treasure Hunt !!")
print("You are in a Island , This is 2 two island in front of you (Right or Left) :")
newIsland = input("Enter l or r to go to new island : ")

if newIsland == "l":
    print("Welcome to Yellow Island !!")
    print("There is a place with 3 doors with painted red , yellow and blue")
    op = input("Select the door by (R,Y,B) : ").lower()
    if op == "r":
        print("WRONG door its on fire 🔥🔥🔥")
    elif op == "y":
        print("You won the GOLD 💛🪙")
    elif op =="b":
        print("WRONG door its full of water 🌊🌊🌊")
    else :
        print("Enter vaild input !!")

else:
    print("Welcome to Red Island !!")
    print("There is a place with 3 doors with painted red , yellow and blue")
    op = input("Select the door by (R,Y,B) : ").lower()
    if op == "r":
        print("You won the RED MARBLE ⭕💎")
    elif op == "y":
        print("WRONG door its on fire 🔥🔥🔥")
    elif op =="b":
        print("WRONG door its full of water 🌊🌊🌊")
    else :
        print("Enter vaild input !!")