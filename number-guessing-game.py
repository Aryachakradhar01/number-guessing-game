import random

guess_random_number = random.randint(1, 99)

while True:
   try:
      user_input = int(input("Guess the number between 1 and 99: "))
   except ValueError:
      print("Please enter a valid number.")
      continue

   if user_input < guess_random_number:
      print("Your guess is too low!!!")
   elif user_input > guess_random_number:
      print("Your guess is too high!!!")
   else:
      print("Congratulations!!!! YOU guessed it right.")
      break
