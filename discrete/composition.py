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


class Alias(object):
    class Bivalued(object):
        def __init__(self, j, i, p):
            self.j = j + 1
            self.i = i + 1
            self.p = p
            self.q = 1 - p

        def random(self, V):
            if V < self.p:
                return self.j
            else:
                return self.i

    def __init__(self, p, n):
        self.n = n
        self.Xs = [0] * (n + 1)

        # Multiplicar por (n - 1) a p
        for i in range(len(p)):
            p[i] = p[i] * (n - 1)

        for k in range(1, n):
            # Tomar el menor (j) y el mayor valor (i) en p
            positive_p = [x for x in p if x > 0]

            min_p = min(positive_p)
            j = p.index(min_p)

            max_p = max(positive_p)
            i = p.index(max_p)

            self.Xs[k] = self.Bivalued(j, i, min_p)

            p[j] -= min_p
            p[i] -= 1 - min_p

    def random(self):
        """Get a random number with distribution p.

        This method is used when generating random variables with a finite
        number of values, say {1, ..., n}.

        """

        I = int(random() * (self.n - 1)) + 1
        V = random()

        return self.Xs[I].random(V)


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

    print('\nAliasing')
    p = [7/16, 1/4, 1/8, 3/16]
    print(sum([p[i] * (i + 1) for i in range(len(p))]))
    a = Alias(p, len(p))
    print(mean(lambda: a.random()))
