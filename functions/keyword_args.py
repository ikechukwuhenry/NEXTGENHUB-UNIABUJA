# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Joel", 29)

# by keyword arguments
printinfo(name="benson", age = 30)

# Function with default Argument
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# calling a function with default argument
printinfo( name="Moses" )

# calling the same function 
printinfo( age=50, name="Moses" )
