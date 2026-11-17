import math


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


def sqrt(x):
    if x < 0:
        raise ValueError("cannot take the square root of a negative number")
    return math.sqrt(x)


def percent(part, whole):
    if whole == 0:
        raise ValueError("cannot take a percent of zero")
    return part / whole * 100


def average(nums):
    nums = list(nums)
    if not nums:
        raise ValueError("cannot take the average of an empty list")
    return sum(nums) / len(nums)
