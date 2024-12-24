# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16]


# Adding corresponding elements from two lists
# list1 = [1, 2, 3]
# list2 = [4, 5, 6,7]
# sum_list = list(map(lambda x, y: x + y, list1, list2))
# print(sum_list)  # Output: [5, 7, 9]

# Converting a list of strings to integers
# str_numbers = ["1", "2", "3", "4"]
# int_numbers = list(map(int, str_numbers))
# int_numbers = list(map(float, str_numbers))
# print(int_numbers)  # Output: [1, 2, 3, 4]

# # Extracting names from a list of dictionaries
# people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
# names = list(map(lambda person: person['name'], people))
# print(names)  # Output: ['Alice', 'Bob']

# import math

# Calculating the square root of each number
# numbers = [4, 16, 25, 36]
# roots = list(map(math.sqrt, numbers))
# print(roots)  # Output: [2.0, 4.0, 5.0, 6.0]

# from itertools import chain

# # Flattening a list of lists
# nested_list = [[1, 2], [3, 4], [5]]
# flattened = list(chain(*nested_list))
# print(flattened)  # Output: [1, 2, 3, 4, 5]

import pandas as pd

# Transforming a column in a DataFrame
df = pd.DataFrame({'values': ['a', 'b', 'c']})
df['upper_values'] = df['values'].map(str.upper)
print(df)
# Output:
#   values upper_values
# 0      a            A
# 1      b            B
# 2      c            C



# Applying a conditional transformation
grades = [95, 67, 85, 76]
performance = list(map(lambda x: 'Pass' if x >= 70 else 'Fail', grades))
print(performance)  # Output: ['Pass', 'Fail', 'Pass', 'Pass']
