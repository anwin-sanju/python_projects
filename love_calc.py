print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
name1 = name1.lower()
name2 = name2.lower()
full_name = name1+name2
t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")
first=t+r+u+e
l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
ee = full_name.count("e")
second=l+o+v+ee
love_score = int(str(first)+str(second))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")