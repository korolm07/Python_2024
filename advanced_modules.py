#Datetime

import datetime 
x = datetime.time (14,20)
#print (x.minute)
today = datetime.date.today ()
#print (today.year)
from datetime import datetime
mydatetime = datetime (2021,10,3,14,20,1)
#print (mydatetime)
from datetime import date 
date1 = date (2021,11,3)
date2 = date (2020,11,3)
x = date1 - date2
#print (x)
#print (type (x))
datetime1 = datetime (2021,11,3,22,0)
datetime2 = datetime (2020,11,3,12,0)
y = datetime1 - datetime2
#print (y)

#Math
import math
value = 4.35
print (math.floor(value))
print (math.ceil(value))
math.pi
print (math.e)

import random 
random.seed (101)
q = random.randint (0,101)
print (q)
mylist = list(range(0,20))
print (mylist)

import pdb
x = [1,2,3]
y = 2
z = 3 
result_one = y + z
pdb.set_trace()
result_two = x + z