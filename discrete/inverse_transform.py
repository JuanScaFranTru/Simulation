from random import random


def inverse_transform(p, x):
    """Get a random value given a discrete distribution.

    It is a good idea to sort the values from highest probability to lowest
    probability to minimize the expected number of operations done by the
    algorithm. This can be done using the method sort_by_probability.

    :param p: p[i] is the probability of x[i].
    :param x: list of possible values of the random variable.

    """

    U = random()
    i = 0
    F = p[0]
    while U >= F:
        i += 1
        F += p[i]
    return x[i]


def sort_by_probability(p, x):
    """Get a sorted version of p and x by highest probability.

    :param p: p[i] is the probability of x[i].
    :param x: list of possible values of the random variable.
    :return: a tuple with sorted p and x
    """
    inv_x = {x[i]: i for i in range(len(x))}
    x = sorted(x, key=lambda x: inv_x[x], reverse=True)
    p = sorted(p, reverse=True)
    return p, x


if __name__ == '__main__':
    def mean(g, N=10000):
        return sum([g() for _ in range(N)]) / N

    p = [0.1, 0.2, 0.3, 0.4]
    x = [1, 2, 3, 4]

    p, x = sort_by_probability(p, x)

    print("Inverse transform mean of:")
    print("x: {} \np: {}".format(x, p))
    print(mean(lambda: inverse_transform(p, x)))
