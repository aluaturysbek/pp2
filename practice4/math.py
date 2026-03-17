#1
import math

# Function to convert degrees to radians
def degree_to_radian(degree):
    return math.radians(degree)

# Example usage
degree = 15
radian = degree_to_radian(degree)
print(f"Input degree: {degree}")
print(f"Output radian: {radian}")


#2
# Function to calculate the area of a trapezoid
def trapezoid_area(height, base1, base2):
    return (height * (base1 + base2)) / 2

# Example usage
height = 5
base1 = 5
base2 = 6
area = trapezoid_area(height, base1, base2)
print(f"The area of the trapezoid is: {area}")


#3
# Function to calculate the area of a regular polygon
def polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

# Example usage
sides = 4
length = 25
area = polygon_area(sides, length)
print(f"The area of the polygon is: {area}")


#4
# Function to calculate the area of a parallelogram
def parallelogram_area(base, height):
    return base * height

# Example usage
base = 5
height = 6
area = parallelogram_area(base, height)
print(f"The area of the parallelogram is: {area}")
