import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def guess_number():
  number = random.randint(1,100)
  return number

def compare(guess, number):
  if guess == number:
    return "You win!"
  elif guess > number:
    return "Too high."
  else:
    return "Too low."

def play_game():
  number = guess_number()
  print(f"Pssst, the correct answer is {number}")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5
    
  while attempts > 0 or guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    result = compare(guess, number)
    if result == "You win!":
      print(result)
      return
    else:
      print(result)
      attempts -= 1
      if attempts < 1:
        print("You've run out of guesses, you lose.")

play_game()