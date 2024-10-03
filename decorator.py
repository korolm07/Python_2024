def func ():
    return 1
print (func ())

def hello ():
    return "hello"
greet = hello #here we copied text to great 
print (greet ())

def hello (name= "jose"):
    print ("hello func exectuted")
    def greet ():
        return "it is great inside hello"
    def welcome ():
        return "this is welcome inside hello"
    #greet and welcome we can execute only inside of hello function 
    print ('i will return funtion ')
    if name == "jose":
        return greet
    else: 
        return welcome

#we can return functions: 
my_new_func = hello ('jose')
print (my_new_func())
def cool ():
    def super_cool ():
        return "Im super cool"
    return super_cool
some_func = cool ()
print (some_func())

#here we have function as argument: 
def hello ():
    return "hi Jose!"
def other (some_def_func):
    print ("Other code")
    print (some_def_func())
print (other (hello))

#create decorator: 
def new_decorator (original_func):
    def wrap_func ():
        print ('some extra code, before original function')
        original_func ()
        print ("some code after original func")
    return wrap_func

#if you want to switch off decorator, just add # before @
@new_decorator
def func_needs_decorator ():
    print ("I want to be decorated")
print (func_needs_decorator())
