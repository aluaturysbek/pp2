x = 5
y = "John"
print(x)
print(y)

# casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# type() function 
x = 5
y = "John"
print(type(x))
print(type(y))


# case-sensitive
# variables a and A are not the same



#var name
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# the same value for every vars
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpacking
fruits = ["apple", "banana", "cherry"] #fruits- a collection
x, y, z = fruits
print(x)
print(y)
print(z)

#printing
x = "john"
y = 5
z = 10
w = " is fourteen"
print(y + z) #math op, if both are nums
print(x + w) #prints a long combined var
print(x, w)  #prints them w/space
print(x, y, z) #correct way of printing diff types of vars




#in functions 
x = "awesome" #global var

def myfunc():
  x = "fantastic" #local var, but if..
  global v  # v now global var, declared inside the func
  v = "great"
  print("Python is " + x)

myfunc() #local var is used only when the function is called

print("Python is " + x) #outside of function global var is used



