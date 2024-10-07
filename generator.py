def create_cubes (n):
    result = []
    for x in range (n):
        result.append(x**3)
    return result 
print (create_cubes(10))

#for x in create_cubes (10):
    #print (x)

def create_cubes (n):
    for x in range (n):
        yield x**3
print (create_cubes(10)) # will not work, need to iterate through each number
for x in create_cubes (10):
    print (x)


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
for number in gen_fibon (10):
    print (number)

def simple_gen():
    for x in range (3):
        yield x 
for number in simple_gen():
    print (number)
g = simple_gen ()
print (next(g))
print (next(g))


def gensquares(N):
    for x in range (N):
        yield x**2
for x in gensquares(10):
    print(x)

import random
random.randint(1,10)
def rand_num(low,high,n):
    for x in range (n):
        yield random.randint(low,high)
for num in rand_num(1,10,12):
    print(f"this is your random number {num}")


s = 'hello'
i = iter (s)
for x in i: 
    print (x)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)