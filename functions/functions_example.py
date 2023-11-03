# creating a function we no argument
def greetings():
   "This is docstring of greetings function"
   print ("Welcome to University of Abuja")
#    return

greetings()     # calling a function


# function with parameter/argument
def greetings(name):
   "This is docstring of greetings function"
   print ("Hello {}".format(name))
   return
   
greetings("Daniel")
greetings("Charity")
greetings("Steven")

def add(x,y):
   z=x+y
   return z

a=10
b=20
result = add(a,b)   # Return a value
print ("a = {} b = {} a+b = {}".format(a, b, result))