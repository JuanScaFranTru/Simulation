from random import random
from math import exp

def aprox_sum(g, N, niter=100):
    """Aproximate the sum of g(i) for i in the interval [1, N].

    If the number of iterations is not less than N, then the exact sum is
    returned.

    :param g: A function with domain of natural numbers
    :param N: The upper limit of the summation
    :param niter: The number of iterations of the algorithm (optional)

    """

    if niter >= N:
        return sum(map(g, range(1, N + 1)))

    S = 0
    for i in range(niter):
        # Generate a random number in [1, N]
        j = int(N * random()) + 1

        S += g(j)

    S = S * N / niter
    return S


if __name__ == '__main__':
    N = 10000
    def g(i): return exp(i / N)

    print("\nMonte Carlo. N = 10000, niter = 100")
    print(aprox_sum(g, N))

    print("\nMonte Carlo. Real Value")
    print(aprox_sum(g, N, N))
