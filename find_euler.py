#!/usr/bin/env python

"""Find the first n digits of Euler's number."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys
from decimal import *

# hard limits
max_n = 1000
iterations = 50

def factorial(x):
    """Requires x > 1"""
    result = Decimal(1)
    for i in range(1, x+1):
        result = result * Decimal(i)
    return result

def calcEuler(n):
    euler_sum = Decimal(1)
    for i in range(1, iterations+1):
        euler_sum += Decimal(1) / factorial(i)
    return euler_sum

def main():
    try:
        n = (int)(sys.argv[1])
        if n < 1:
            raise ValueError
        elif n > max_n:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: euler.py [n]")
        print("[n] = number of digits to display, up to 1000")
        sys.exit(1)

    # set precision
    starting_prec = getcontext().prec
    is_n_bigger = (n > getcontext().prec)
    if is_n_bigger:
        getcontext().prec = n
    # get e
    e = calcEuler(n)

    # limit precision if n is smaller
    if not is_n_bigger:
        getcontext().prec = n

    # use slice notation
    e_str = str(e)
    if n == 1:
        print(e_str[0])
    else:
        print(e_str[0:n+1])
    
if __name__ == "__main__":
    main()
