from random import random

def composition(p, F):
    """Simulate variable X = sum([p[i]*F[i] for i in range(len(p))])
    This method is applied when the distribution function can be expressed as a
    linear combination of other distribution functions.

    :param p: List of weights. sum(p[i]) == 1
    :param F: List random number generators with distribution F[i]
    """

    U = random()
    j = 0
    acc = p[j]
    while U >= acc:
        j += 1
        acc += p[j]

    return F[j]()
