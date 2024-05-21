import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_signs = [rock,paper,scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
print(game_signs[user_choice])
computer_choice = random.randint(0,len(game_signs)-1)
print("Computer chose:")
print(game_signs[computer_choice])

if user_choice == computer_choice:
  print("It\'s a draw")
else:
  if user_choice == 0:
    if computer_choice == 1:
      print("You lose")
    else:
      print("You win")
  elif user_choice == 1:
    if computer_choice == 0:
      print("You win")
    else:
      print("You lose")
  elif user_choice == 2:
    if computer_choice == 0:
      print("You lose")
    else:
      print("You win")