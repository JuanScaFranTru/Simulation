from random import random
from discretes import uniform_discrete
from discretes import poisson
from discretes import random_bernoulli


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


if __name__ == '__main__':
    def mean(g, N=10000):
        return sum([g() for _ in range(N)]) / N

    p = [0.1, 0.2, 0.3, 0.4]

    def F1(): return uniform_discrete(0, 10)

    def F2(): return poisson(5)

    def F3(): return random_bernoulli(0.3)

    def F4(): return random_bernoulli(0.5)

    F = [F1, F2, F3, F4]

    print('\nComposition')
    print(mean(lambda: composition(p, F)))

    def random_F():
        return sum([p[i] * F[i]() for i in range(len(p))])

    print('\nNo Composition')
    print(mean(lambda: random_F()))
