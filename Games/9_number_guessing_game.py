import random
print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input ("Choose a difficulty. Type 'easy' or 'hard': ")
x = random.randint(1,100)
print (f"correct is {x}")
if level == "easy": 
  attemps_number = 10
elif level == "hard":
  attemps_number = 5
print (f"You have {attemps_number} attempts remaining to guess the number.")
guess = int(input ("Make a guess: "))
game_over = False
while not game_over:
    if x > guess and attemps_number > 1: 
      print ("Too low")
      attemps_number -=1 
      print (f"You have {attemps_number} attempts remaining to guess the number.")
      guess = int(input ("Guess again: "))
    elif x < guess and attemps_number > 1: 
      print ("Too high")
      attemps_number -=1 
      print (f"You have {attemps_number} attempts remaining to guess the number.")
      guess = int(input ("Guess again: "))
    elif x == guess: 
      print (f"You got it! The answer was {x}")
      game_over = True
    else: 
      print ("You've run out of guesses, you lose.")
      game_over = True
  
