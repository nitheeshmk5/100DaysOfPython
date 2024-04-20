from random import choice
from datas import data

def choose_account(acc):
    return choice(acc)

def highOrLow():
    score = 0
    game = True
    while game:
        one = choose_account(data)
        name1 = one['name']
        country1 = one['country']
        des1 = one['description']
        follow1 = one['follower_count']
        print(f"A) {name1} : {des1} | from {country1}")

        two = choose_account(data)
        if one == two:
            two = choose_account(data)

        name2 = two['name']
        country2 = two['country']
        des2 = two['description']
        follow2 = two['follower_count']
        print(f"B) {name2} : {des2} | from {country2}")

        guess = input("Enter A or B : ").upper()

        if guess == "A" and follow1 > follow2:
            print("Its correct")
            score += 1
            print(f"The score is {score}")
        elif guess =="B" and follow1 < follow2:
            print("Its right")
            score += 1
            print(f"The score is {score}")
        else:
            print("Wrong")
            print(f"The score is {score}")
            game = False

highOrLow()