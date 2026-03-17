#1
def square_generator(N):
    for i in range(N+1):
        yield i**2


N = int(input())
for square in square_generator(N):
    print(square)

# 2
def even_numbers_generator(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
evens = even_numbers_generator(n)
print(", ".join(map(str, evens))) 


#3
def divisible_by_3_and_4(start, n):
    for i in range(start, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

start = int(input())
n = int(input())
for num in divisible_by_3_and_4(start, n):
    print(num)


#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)