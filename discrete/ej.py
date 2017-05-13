from math import exp
from random import random
from permutations import random_permutation
from monte_carlo import aprox_sum


class One(object):
    def a(N=100, niter=100):
        results = One.run_experiments(N, niter)
        print("\n1a.")
        One.print_stats(results, niter)

    def b(N=100, niter=10000):
        results = One.run_experiments(N, niter)
        print("\n1b.")
        One.print_stats(results, niter)

    def run_experiments(N, niter):
        xs = list(range(1, N + 1))
        results = [None] * niter
        for i in range(niter):
            results[i] = One.experiment(xs)
        return results

    def experiment(xs):
        xs = random_permutation(xs)
        successes = 0
        for i in range(len(xs)):
            if xs[i] == (i + 1):
                successes += 1
        return successes

    def mean(xs, N):
        return sum(xs) / N

    def variance(xs, N):
        return One.mean(map(lambda x: x ** 2, xs), N) - One.mean(xs, N) ** 2

    def print_stats(xs, N):
        mean = round(One.mean(xs, N), 2)
        variance = round(One.variance(xs, N), 2)
        print("Mean: {} \t Variance: {}".format(mean, variance))


class Two(object):
    def run_all(N=10000, niter=100):

        def g(k): return exp(k / N)

        S = round(aprox_sum(g, N, niter), 2)

        print("\n2.")
        print("Estimated Sum = ", S)

        S_real = round(aprox_sum(g, N, N), 2)
        print("Real Sum = ", S_real)
        error = round(abs(S_real - S) * 100 / S, 2)
        print("Error = {}%".format(error))


class Three(object):
    def run_all():
        print("\n3.")
        for niter in [100, 1000, 10000, 100000]:
            results = Three.run_experiments(niter)
            One.print_stats(results, niter)

    def run_experiments(niter):
        results = [None] * niter
        for i in range(niter):
            results[i] = Three.experiment()
        return results

    def experiment():
        nfaces = 6  # number of faces of a dice
        bitmap = {i: False for i in range(2, 12)}
        nrolls = 0
        while not all(bitmap.values()):
            U = int(nfaces * random()) + 1
            V = int(nfaces * random()) + 1
            U + V
            bitmap[U + V] = True
            nrolls += 1
        return nrolls


class Four(object):
    def compute_poisson(lambda_, k):
        assert lambda_ <= 745, 'Lambda too big!'
        p = [0] * (k + 1)
        p[0] = exp(-lambda_)

        for j in range(1, k + 1):
            p[j] = p[j - 1] * lambda_ / j

        return p

    def compute_distribution(lambda_, k):
        p = Four.compute_poisson(lambda_, k)
        s = sum(p)
        for i in range(len(p)):
            p[i] = p[i] / s

        return p

    def a(lambda_=100, k=1000, niter=100):
        p = Four.compute_distribution(lambda_, k)
        print("\n4a.")
        results = [Four.random_inverse_transform(p) for _ in range(niter)]
        One.print_stats(results, niter)

    def random_inverse_transform(p):
        U = random()
        F = 0
        for i, x in enumerate(p):
            F += x
            if U < F:
                return i
        return len(p) - 1  # In case sum(p) < 1.0

    def b(lambda_=100, k=1000, niter=100):
        p = Four.compute_distribution(lambda_, k)
        print("\n4b.")
        results = [Four.random_accept_and_reject(p) for _ in range(niter)]
        One.print_stats(results, niter)

    def random_accept_and_reject(lambda_, p):
        s = sum(p)
        while True:
            Y = poisson_optimized(lambda_)
            U = random()
            if U < p(Y) * s / p(Y):
                break
        return Y


if __name__ == '__main__':
    One.a()
    One.b()
    Two.run_all()
    Three.run_all()
    Four.a()
    Four.b()
