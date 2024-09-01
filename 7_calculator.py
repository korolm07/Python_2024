def add (n1, n2):
  return n1+n2
def substract (n1, n2):
  return n1-n2
def multiply (n1, n2):
  return n1*n2
def divide (n1, n2):
  return n1/n2

operations = {
"+" : add,
"-" : substract,
"*" : multiply,
"/" : divide
}

num1 = int(input("type 1st number  "))
num2 = int(input("type 2nd number  "))

for symbol in operations:
  print(symbol)
operation_symbol = input ("Select operator from above  ")

calculation_function = operations[operation_symbol]
answer = calculation_function (num1,num2)
print (f"{num1} {operation_symbol} {num2} = {answer}")
