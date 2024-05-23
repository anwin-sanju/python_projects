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

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  
def play_game(): 
    user_cards = []
    computer_cards = []
    is_gameover = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_gameover:
        user_score = calculate_score(cards=user_cards)
        computer_score = calculate_score(cards=computer_cards)

        print(f"Your cards are {user_cards} and score is {user_score}.")
        print(f"Computer's first card is {user_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameover = True
        else:
            user_should_continue = input("Do you want to draw another card? Type 'y' or 'n': ")
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and final score is {user_score}.")
    print(f"Computer's final hand is {computer_cards} and final score is {computer_score}")

    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()