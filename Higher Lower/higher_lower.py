import random
from game_data import data

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

from art import logo
print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")

from art import vs
print(vs)

print(f"Against B: {format_data(account_b)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]