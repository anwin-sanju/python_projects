### Test ###

import random

from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
def deal_card():
  return random.choice(cards)

user_bet = int(input("How much do you want to bet? $"))
  
user_cards = []
computer_cards = []

if should_play == "y":
  for i in range(0,2):
    user_choice = deal_card()
    user_cards.append(user_choice)
    computer_choice = deal_card()
    computer_cards.append(computer_choice)
else:
  print("Goodbye")

print(f"User got : {user_cards}")
print(f"Computer got :{computer_cards}")

def add(cards_list):
  sum = 0
  for i in cards_list:
    sum += i
  print(sum)
  return sum

if user_cards == [11,10] or user_cards == [10,11]:
  print("User got a blackjack")
elif computer_cards == [11,10] or computer_cards == [10,11]:
  print("Computer got a blackjack")

user_total = add(user_cards)
computer_total = add(computer_cards)

if user_total > 21:
  for i in user_cards:
    if i == 11:
      i = 1
      user_total = add(user_cards)
    else:
      print("User loses")
elif computer_total > 21:
  for i in computer_cards:
    if i == 11:
      i = 1
      computer_total = add(computer_cards)
  print("Computer loses")

def compare(user_total, computer_total):
  if user_total > computer_total:
    print("User wins")
  elif computer_total > user_total:
    print("Computer wins")
  elif user_total == computer_total:
    print("Draw")

compare(user_total=user_total, computer_total=computer_total)

should_continue = input("Do you want to draw another card? Type 'y' or 'n': ")
if should_continue == "y":
  user_choice = deal_card()
  user_cards.append(user_choice)
  computer_choice = deal_card()
  computer_cards.append(computer_choice)
  print(f"User got : {user_cards}")
  print(f"Computer got :{computer_cards}")
  user_total = add(user_cards)
  print(user_total)

compare(user_total=user_total, computer_total=computer_total)