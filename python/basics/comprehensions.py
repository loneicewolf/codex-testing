"""Showcases list and dictionary comprehensions."""

# List comprehension to create squares
squares = [n * n for n in range(5)]
print("List of squares:", squares)

# Dictionary comprehension for mapping numbers to their cubes
cubes = {n: n ** 3 for n in range(5)}
print("Dictionary of cubes:", cubes)

# Set comprehension for unique characters in a string
unique_chars = {c for c in "hello world" if c != ' '}
print("Unique characters:", unique_chars)

