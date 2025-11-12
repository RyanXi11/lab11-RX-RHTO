"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def log(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError
    return a ** 0.5
def hyp(a, b):
    return (a ** 2 + b ** 2) ** 0.5

