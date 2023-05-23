# local variable in function
# a local variable is a variable that is declared inside a function

def akum():
    a = 12
    print('this is a local variable', a)


def emma():
    b = 10
    print("the value is", b)


# call function
akum()
emma()

# Global Variable
y1 = 600


def Acha():
    print(y1)


Acha()


def blaise():
    y2 = y1+20
    print(y2-4)


blaise()


# Write a Python function called calculate_factorial that takes a positive integer as input and calculates its factorial using a loop.

# The factorial of a number n is the product of all positive integers from 1 to n.
def calculate_factorial(n):
    factorial = 1

    # Check if the input is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    # Calculate the factorial using a loop
    for i in range(1, n + 1):
        factorial *= i

    return factorial

number = 5
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}.")