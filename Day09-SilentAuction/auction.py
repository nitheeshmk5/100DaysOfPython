import os

auctioners = {}

def high_bid(bidders):
      high = 0
      winner = ""

      for i in bidders:
            bid_amt = bidders[i]
            if bid_amt > high:
                  high = bid_amt
                  winner = i
      print(f"The winner is {winner} with amount {high}")

over = False
while not over:
      name = input("Enter name : ")
      amt = float(input("Enter bit amount : "))
      auctioners[name] = amt
      again = input("Enter 'Y' for another bit else 'N' : ").upper()
      if again == 'N':
            over = True
            high_bid(auctioners)
      elif again == 'Y':
            os.system('cls')
            
print(f"Total bids are : {auctioners}")