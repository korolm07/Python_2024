x = 5
y = 0
try: 
    z = x/y
except: 
    print ("wrong numbers")
finally: 
    print ("All Done")

def ask():
    while True: 
        try: 
            a = int (input ("Provide number "))
            b = a**2
        except: 
            print ("An error occurred! Please try again!")
            continue
        else:
            print (f"Thank you, your number squared is: {b}")
            break
ask ()