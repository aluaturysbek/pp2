# Example usage of enumerate to get index and value
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")





names = ['Alice', 'Bob', 'Charlie']
ages = [24, 30, 18]

# Using zip to pair up names and ages
paired = zip(names, ages)

# Convert to list and print
print(list(paired))