import random as rd

print("Welcome to Nitheesh's guess the number !!")
level = input("Choose the level (easy or hard) : ").lower()
no_of_attempts = 10
if level == "hard":
    no_of_attempts = 5

number = rd.randint(1,100)

while no_of_attempts > 0:
    print(f"Number of chance is {no_of_attempts}")
    guess = int(input("Guess a number : "))
    if guess < number:
        print("Low")
        no_of_attempts -= 1
    elif guess > number:
        print("High")
        no_of_attempts -=1
    else:
        print(f"You won !! Number is {number}")
        break
    
