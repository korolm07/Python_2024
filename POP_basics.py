class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return Cylinder.pi*self.radius**2*self.height
    def surface_area(self):
        return 2*Cylinder.pi*self.radius*self.height + 2*Cylinder.pi*self.radius**2
c = Cylinder(2,3)
print (c.volume())
print (c.surface_area ())

from math import sqrt
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print (li.distance())
print(li.slope())


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit (self, deposit_amount):
        self.balance += deposit_amount  
        print (f"Deposit Accepted.Current balance is {self.balance}")
    def withdraw (self, withdraw_amount):
        if self.balance < withdraw_amount:
            print ("Funds Unavailable!")
        else: 
            self.balance -= withdraw_amount 
            print (f"Withdrawal Accepted. Current balance is {self.balance}")
    def __str__(self):
        return f"Owner is: {self.owner}\nBalance is {self.balance}"
act1 = Account ("Jack",100)
act1.deposit (200)
act1.withdraw (800)
print (act1)