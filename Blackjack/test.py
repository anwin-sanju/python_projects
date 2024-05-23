import random
from art import logo
print(logo)

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

user_cards = []
computer_cards = []

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
     return 0
  return sum(cards)