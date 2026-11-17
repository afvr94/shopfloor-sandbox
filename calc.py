def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def mod(a, b):
    if b == 0:
        raise ValueError("cannot take modulo by zero")
    return a % b
