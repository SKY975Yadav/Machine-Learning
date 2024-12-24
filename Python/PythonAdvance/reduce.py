from functools import reduce

# # Finding the maximum element
# numbers = [1, 5, 3, 9, 2]
# max_value = reduce(lambda x, y: x if x > y else y, numbers)
# print(max_value)  # Output: 9

# # Concatenating strings in a list
# words = ["Hello", "World", "from", "Python"]
# sentence = reduce(lambda x, y: x + " " + y, words)
# print(sentence)  # Output: "Hello World from Python"

# Flattening a list of lists
# nested_list = [[1, 2], [3, 4], [5]]
# flattened = reduce(lambda x, y: x + y, nested_list)
# print(flattened)  # Output: [1, 2, 3, 4, 5]

# Calculating the product of all numbers in a list
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 24

# Calculating factorial of n
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n+1))
print(factorial)  # Output: 120

