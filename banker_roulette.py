import random
names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names = names_string.split(", ")
unlucky_number = random.randint(0,len(names)-1)
unlucky_guy = names[unlucky_number]
print(f"{unlucky_guy} is going to buy the meal today!")