# Create two variables x and y, and initially set them each to a different number. Write a python function that swaps both values.
# Example: x = 10, y = 20
# Output: x = 20, y = 10

# method 1 using a function

def swap_values(x, y):
    # changing the values
    x, y = y, x
    return x, y


# Initial values
x = 10
y = 20

# Calling the function to change or swaps values
x, y = swap_values(x, y)

# Printing the changing or swapped values
print("x =", x)
print("y =", y)

# method 2 as a script

x = 10
y = 20

print("Before swap:")
print("x =", x)
print("y =", y)

# Swapping the values
swap = x
x = y
y = swap

print("After swap:")
print("x =", x)
print("y =", y)
