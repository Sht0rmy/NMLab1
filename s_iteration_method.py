import math
from sympy import symbols
import common
import sys


def method(x0,alpha,epsilon):
    x = sys.maxsize
    x1 = x0
    iteration = 0
    while abs(x1-x) > epsilon:
        x = x1
        x1 = common.phi_func(x,alpha)

        print('{:<2d}: [x: {:<10f}, f(x): {:<10f}]'.format(iteration, x, x1))

        iteration = iteration + 1
    return x1, iteration

