import random as rand

# Squares of numbers from 1 to 5
# squares = [x**3 for x in range(1, 6)if x % 2 != 0]
# print(squares)

# # Dictionary : 
# squares = {x : x**2 for x in range(1, 6)if x % 2 != 0}
# print(squares)

# # Creating a generator comprehension for squares of even numbers from 1 to 10
# even_squares_gen = (x**2 for x in range(1, 11) if x % 2 == 0)

# # Iterating through the generator using a loop
# print("Squares of even numbers from 1 to 10:")
# for square in even_squares_gen:
#     print(square)


# # For 2 variabes : 

# res = [x*y for x in range(1,4) for y in range(1,6) if x < y]
# print(res)
# # [2, 3, 4, 5, 6, 8, 10, 12, 15]

# res1 = {(x,y):x*y for x in range(1,4) for y in range(1,6) if x < y}
# print(res1)
# # {(1, 2): 2, (1, 3): 3, (1, 4): 4, (1, 5): 5, (2, 3): 6, (2, 4): 8, (2, 5): 10, (3, 4): 12, (3, 5): 15}


# # If else
# # Assign 'even' or 'odd' based on the number
# labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
# print(labels)
# # Output: ['odd', 'even', 'odd', 'even', 'odd']


# nums = [rand.randint(1,100) for _ in range(50)]
# print(nums)

# import numpy as np

# # Generate 50 random numbers between 1 and 100
# random_numbers = np.random.randint(1, 101, 50)

# print(random_numbers)

import random

# def generate_random_numbers(n, start, end):
#     for _ in range(n):
#         yield random.randint(start, end)

# random_numbers = list(generate_random_numbers(20, 1, 100))

# print(random_numbers)

# res = ['even' if x%2==0 else 'odd' for x in random_numbers]
# print(res)


# Multiplication table (1 to 3) as a 2D list
table = [[x * y for y in range(1, 4)] for x in range(1, 5)]
print(table)
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# Applying a custom function inside a comprehension
def square(x):
    return x**2

squared_numbers = [square(x) for x in range(1, 6)]
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

# Only even numbers from 1 to 10 that are also greater than 5
filtered = [x for x in range(1, 11) if x % 2 == 0 if x > 5]
print(filtered)
# Output: [6, 8, 10]

# Cartesian product of two lists
list1 = [1, 2, 3]
list2 = ['a', 'b']
cartesian_product = [(x, y) for x in list1 for y in list2]
print(cartesian_product)
# Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

 # Dictionary with index as key and square as value
squared_indexed = {i: x**2 for i, x in enumerate(range(1, 6))}
print(squared_indexed)
# Output: {0: 1, 1: 4, 2: 9, 3: 16, 4: 25}

# Mapping two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict)
# Output: {'a': 1, 'b': 2, 'c': 3}

