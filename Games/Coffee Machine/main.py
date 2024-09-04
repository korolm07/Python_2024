import menu

resources = {
  'water': 300,
  'milk': 200,
  'coffee': 100,
}

collected_money = 0
shouldcontinue = True


def is_resource_sufficient(order_ingredients):
  for item in order_ingredients:
      if order_ingredients[item] > resources[item]:
          print(f"Sorry there is not enough {item}.")
          return False
      else:
        return True

def compare_money ():
  if change > 0: 
    return True
  else: 
    return False

while shouldcontinue:
  answer = input("What would you like? ☕ espresso, latte or cappuccino? ")
  if answer in menu.MENU:
    drink = menu.MENU [answer]
    if is_resource_sufficient(drink["ingredients"]):
      print ("Please insert coins.")
      total = int(input ("How many quarters?: ")) * 0.25
      total += int(input ("How many dimes?: ")) *0.1
      total += int(input ("How many nickles?: ")) * 0.05
      total +=  int(input ("How many pennies?: ")) * 0.01
      change = round(total - menu.MENU [answer]["cost"],2)
      if compare_money () == True:
        print (f"Here is {change} in change. \nHere is your {answer}. Enjoy!")
        collected_money += menu.MENU [answer]["cost"]
        for item in drink["ingredients"]:
          resources[item] -= drink["ingredients"][item]
      elif compare_money () == False: 
        print ("Sorry that's not enough money. Money refunded.")
  elif answer == "report":
    print (f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources ['coffee']}\nMoney: {collected_money}")
  elif answer == "off":
    print ("turning off")
    shouldcontinue = False 
  elif answer not in menu.MENU:
    print ("Please check spelling. If spelling is correct, means item is not in Menu")
  else: 
    print ("Sorry that item is not available. Please select another item. Type 'report' to see available resorces.")




  
