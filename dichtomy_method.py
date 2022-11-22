import math
import common


def apriori_assessment(a, b, epsilon):  # n_0(eps) = [log_2((b - a) / eps)] + 1
    if not common.sign_change_condition(a, b):
        return None
    return math.floor(math.log2((b - a) / epsilon)) + 1


def method(a, b, epsilon):
    if not common.sign_change_condition(a, b):
        return None, None

    iteration = 0
    x = a
    while True:
        x = (b + a) / 2

        print('{:<2d}: [a: {:<10f}, b: {:<10f}]'.format(iteration, a, b))

        if common.sign_change_condition(a, x):
            b = x
        else:
            a = x

        iteration = iteration + 1
        if iteration != 0 and common.termination_condition(a, b, epsilon):
            break

    return x, iteration
