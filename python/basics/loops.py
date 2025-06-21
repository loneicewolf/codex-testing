"""Examples demonstrating loop constructs in Python."""

# For loop over a list
print("For loop over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("  ", fruit)

# While loop with a counter
print("\nWhile loop counting down:")
count = 3
while count > 0:
    print("  ", count)
    count -= 1
print("  Blast off!")

# Looping over a dictionary
print("\nLooping over a dictionary:")
ages = {"Alice": 30, "Bob": 25, "Carol": 27}
for name, age in ages.items():
    print(f"  {name} is {age} years old")

