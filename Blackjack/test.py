import random
from art import logo
print(logo)

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
     return 0
  if 11 in cards and sum(cards) > 21:
     cards.remove(11)
     cards.append(1)
  return sum(cards)

user_cards = []
computer_cards = []
is_gameover = False

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(cards=user_cards)
computer_score = calculate_score(cards=computer_cards)

print(f"Your cards are {user_cards} and score is {user_score}.")
print(f"Computer's first card is {user_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
   is_gameover = True