import random

deck = {
    'king👑': 10, 'queen👑': 10, 'jack♟️': 10, 'ten🔟': 10, 'nine9️⃣': 9, 'eight8️⃣': 8,
    'seven7️⃣': 7, 'six6️⃣': 6, 'five5️⃣': 5, 'four4️⃣': 4, 'three3️⃣': 3, 'two2️⃣': 2,
    'ace🅰️': 11
}
deck_keys = list(deck.keys())


def pass_card(cards, no_cards):
    return random.sample(cards, no_cards)


print("Welcome to Blackjack with Nitheeshmk ♠️♥️♦️♣️🃏")
player_name = input("Enter your username : ")
balance = 1000
bet_amount = 0

while True:
    print(f"Starting balance ==>  {balance}rs")
    bet_amount = int(input("Enter the amount to bet : "))
    while bet_amount < 1 or bet_amount > balance:
        print("Invalid amount 😟 !! Try again ")
        print("")
        bet_amount = int(input("Enter a valid amount to bet : "))

    # assigning card to veerargal (players)

    player_hand = pass_card(deck_keys, 2)
    dealer_hand = pass_card(deck_keys, 2)

    # total value in their hand

    player_value = deck[player_hand[0]] + deck[player_hand[1]]
    dealer_value = deck[dealer_hand[0]] + deck[dealer_hand[1]]

    print(f"{player_hand} ==> {player_value}")

    # game logic
    if player_value == 21 and len(player_hand) == 2:
        print("BlackJack !!! You won")
        balance = balance + (bet_amount * 2)
        print(f"Your balance is {balance}💸 ")
    else:
        while player_value < 21:
            choice = input("Want to hit or stop ? (hit / stop) : ").lower()
            if choice == 'hit':
                player_hand.extend(pass_card(deck_keys, 1))
                player_value += deck[player_hand[-1]]
                print(f"{player_hand} ==> {player_value}")
            elif choice == 'stop':
                break

        # dealer's chance
        while dealer_value < 17:
            dealer_hand.extend(pass_card(deck_keys, 1))
            dealer_value += deck[dealer_hand[-1]]

        print("")
        print("Results !! ")
        if player_value > 21:
            print("Bust !! You lose 😔")
            print(f"Your cards : {player_hand}\nYour value ==> {player_value}")
            balance -= bet_amount

        elif dealer_value > 21 or player_value > dealer_value:
            print('You win !! 🥂🥳')
            print(f"Your cards : {player_hand}\nYour value ==> {player_value}")
            print(f"Dealer's cards : {dealer_hand}\nYour value ==> {dealer_value}")
            balance += bet_amount

        elif player_value == dealer_value:
            print("It's a tie !!")
            print(f"Dealer's cards : {dealer_hand}\nYour value ==> {dealer_value}")
            print(f"Your cards : {player_hand}\nYour value ==> {player_value}")

        else:
            print('You lose.')
            balance -= bet_amount

    print("")
    print(f"Your balance is {balance}💸 ")
    print("")
    play_again = input(f"Good game {player_name} , want to play again ? (yes/no) : ").lower()
    if play_again == 'no':
        break

print("")
print(f"Well played {player_name}!! Thanks for playing 🤍\nFinal balance : {balance}rs")
