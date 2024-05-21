def prime_checker(number):
  counter = 0
  if number <= 1:
    print("It's not a prime number.")
  for i in range(2,number+1):
    if number % i == 0:
      counter += 1
  if counter > 1:
    print("It's not a prime number.")
  else:
    print("It's a prime number.")

n = int(input())
prime_checker(number=n)