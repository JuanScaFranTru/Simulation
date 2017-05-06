from random import random


def accept_and_reject(Y_random, c, p, q):
    """Get a random number using the accept and reject method.

    Given a target random variable X to be simulated let Y be a random variable
    for which holds:

    - Y_random is a random number generator with the same distribution as Y.
    - if p(j) > 0, then q(j) > 0 for all x(j) in the range of X.
    - Exists a positive constant c such that p(j)/q(j) = c.

    Where p(j) = P(X = x(j)) and q(j) = P(Y = x(j))

    Let f be the PDF (or pmf) of X and g the PDF (or pmf) of Y.
    The main idea is to look at the tail of f(x). That is how does f(x) behave
    when x is very large. Then we need to find something that looks like it,
    but is easy to integrate.

    We want to keep g as close to f as possible If M is high we reject a lot of
    samples. Once we choose a g, we integrate it from x to infinity and divide
    that by the integral from 0 to infinity (to avoid having)
    """
    while True:
        Y = Y_random()
        U = random()
        if U < p(Y) / c * p(Y):
            break
    return Y


if __name__ == '__main__':
    pass
