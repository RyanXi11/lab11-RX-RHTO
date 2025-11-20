"""https://github.com/RyanXi11/lab11-RX-RHTO/tree/main
Partner 1: Ryan Xi
Partner 2: Rafael Hitoshi Teixeira Oura

calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.



"""
import math


def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if b <= 0:
        raise ValueError
    if a <= 0 or a == 1:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError
    return a ** 0.5
def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5


