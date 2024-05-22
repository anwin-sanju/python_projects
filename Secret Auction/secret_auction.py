import os
from art import logo
print(logo)

bids = {}

finished = False

while not finished:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  bids[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if more_bidders == "no":
      finished = True
      clear = lambda: os.system('clear')
      clear()
  for bidder in bids:
    highest_bid = 0
    winner = ""
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")