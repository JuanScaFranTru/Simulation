from math import exp
from random import random


def accept_and_reject(Y_random, c, p, q):
    """Get a random number using the accept and reject method.
    """
    while True:
        Y = Y_random()
        U = random()
        if U < p(Y) / (c * q(Y)):
            break
    return Y


def bla(x):
    return x * exp(-x)


a = sum([accept_and_reject(random, exp(-1), bla,
                           lambda x: 1) for i in range(10000)]) / 10000

print(a)
