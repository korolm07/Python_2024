import random
#from replit import clear  
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice (cards) 
  return card
  

def calculate_score (cards):
  if sum (cards) == 21 and len(cards) == 2: 
    return 0 
  elif sum (cards) > 21 and cards == 11:
    cards.remove (11)
    cards.append (1)
  return sum(cards)
def compare (u_score, c_score):
  if u_score == c_score:
    print ("draw")
  elif c_score == 0:
    print ("Computer has blackjack, you lose")
  elif u_score == 0: 
    print ("You win with blackjakc")
  elif u_score > 21:
    print ("over 21, you lose")
  elif c_score > 21: 
    print ("Computer over 21, you win")
  elif c_score > u_score:
    print ("Computer has higher score")
  elif u_score > c_score:
    print ("You has higher score")
    
def play_game (): 
  game_end = False
  user_cards = []
  computer_cards = []
  for _ in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not game_end:
    user_score = calculate_score (user_cards)
    computer_score = calculate_score (computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21: 
      game_end = True
    else:
      question = input("Do you want another card: y or n?")
      if question == "y":
        user_cards.append(deal_card())
      else: 
        game_end = True
  while computer_score != 0 and computer_score < 17: 
    computer_cards.append(deal_card())
    computer_score = calculate_score (computer_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
    
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  #clear()
  play_game()
