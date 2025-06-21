"""Demonstrates Python lambda functions and higher-order operations."""

# Simple lambda for squaring a number
square = lambda x: x * x
print("Square of 5:", square(5))

# Using lambda with map
nums = [1, 2, 3, 4]
squared = list(map(lambda n: n * n, nums))
print("Squared list via map:", squared)

# Using lambda with filter
odd = list(filter(lambda n: n % 2 == 1, nums))
print("Odd numbers via filter:", odd)

# Sorting with a lambda key
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
pairs.sort(key=lambda p: p[1])
print("Pairs sorted by second element:", pairs)

