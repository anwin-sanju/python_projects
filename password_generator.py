import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for i in range(1, nr_letters+1):
    random_letter_num = random.randint(0,len(letters))
    print(letters[random_letter_num])
    password_list.append(letters[random_letter_num])

for k in range(1, nr_numbers+1):
    random_number_num = random.randint(0,len(numbers))
    print(numbers[random_number_num])
    password_list.append(numbers[random_number_num])

for l in range(1, nr_symbols+1):
    random_symbols_num = random.randint(0,len(symbols))
    print(symbols[random_symbols_num])
    password_list.append(symbols[random_symbols_num])

print(password_list)