import random
from database import data
#import clear
score = 0
random_b = random.choice (data)

print ("Welcome to game LowHighGuess")
should_continue = True
while should_continue: 
  random_a = random_b
  random_b = random.choice (data)
  if random_a == random_b:
     random_b = random.choice (data)
  print (f"Compare A: {random_a['name']}, a {random_a['description']} from {random_a['country']}")
  print (f"Against B: {random_b['name']}, a {random_b['description']} from {random_b['country']}")

  answer = input("Who has more followers? Type 'A' or 'B': ").capitalize ()
  print("\n"*20)
  def compare ():
    if (random_a['follower_count']) > (random_b['follower_count']):
      return answer == "A"
    else:
      return answer == "B"
  if compare() == True: 
    score +=1 
    print (f"You're right! Current score: {score}") 
  else:
    print (f"Sorry, that's wrong. Final score: {score}")
    should_continue = False
    
    
