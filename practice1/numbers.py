x = 1    # int
y = 2.8  # float
z = 1j   # complex
num = 5e45 # e means power of ten, theyre floats

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x) #1.0
print(y) #2
print(z) #1 + 0j

print(type(x))
print(type(y))
print(type(z))



#random module
import random
print(random.randrange(1, 10)) #where [1,10)



