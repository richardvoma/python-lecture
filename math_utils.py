def add(a, b):
    "Addition of two numbers."
    return a + b


def subtract(a, b):
    "Subtraction of two numbers."
    return a - b


def multiply(a, b):
    "Multiplication of two numbers."
    return a * b


def divide(a, b):
    "Division of two numbers."
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")
