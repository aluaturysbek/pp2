# Example function that doubles a number
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled = map(double, numbers)

# Convert to list and print
print(list(doubled))


# Example function that filters out even numbers
def is_odd(x):
    return x % 2 != 0

numbers = [1, 2, 3, 4, 5, 6]
odds = filter(is_odd, numbers)

# Convert to list and print
print(list(odds))



from functools import reduce

# Example function that multiplies two numbers
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
result = reduce(multiply, numbers)

print(result)