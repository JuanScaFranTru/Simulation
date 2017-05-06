from random import random
from math import log
from math import exp


def uniform_discrete(m, k):
    """Discrete Uniform distribution.

    Given that the algorithm will output j if and only if:

        (j-1)/n <= U(0, 1) <= j/n

    U belongs to [(j-1)/n, j/n) iff n * U belongs to [j-1, j]. But this
    will occur if and only if:

        j = floor(n * U) + 1

    given that int(n * U) is the same as floor(n * U), we obtain:

        j = int(n * U) + 1

    Get a random natural number in the interval [m, k].
    """
    U = random()
    return int(U * (k - m + 1)) + m


def random_geometric(p):
    """Get a geometrically distributed random number with parameter p.

    This is a result obtained by applying the inverse transform method to the
    geometric distribution:

        P(X = i) = p * q**(i-1) for i >= 1, q = (1-p)

    Then the accumulated distribution is:

        Fx(j-1) = P(X <= j-1) = 1 P(X > j-1) = 1 - q**(j-1)

    The inverse transform method then assigns X = j iff:

        U belongs to [1 - q**(j-1), 1 - q**j)

    But this happens iff:

        1 - q**(j-1) <= U < 1 - q**j

        q**j < 1 - U <= q**(j-1)

        j = min{k: q**k < 1 - U} (Note that the powers of q decrease as k gets
        bigger (0 < q < 1).)

        X = min{k | k * log(q) < log(1 - U)}

        X = min{k | k > log(1 - U) / log(q)}  log(q) < 0

        X = min{k | k > log(V) / log(q)}      if U ~ U(0,1) then V=1-U ~ U(0,1)

        X = floor(log(V) / log(q)) + 1

        X = int(log(random()) / log(1 - p)) + 1
    """
    return int(log(random()) / log(1 - p)) + 1


def random_bernoulli(p):
    """Get a Bernoulli distributed random number with parameter p.
    """
    U = random()

    if U < p:
        return 1
    else:
        return 0


def random_bernoulli_batch(p, N):
    """Get N Bernoulli distributed random numbers with parameter p.

    This method is efficient for large N.
    """

    result = [0] * N

    M = 0
    while True:
        B = random_geometric(p)
        M += B
        if M - 1 >= N:
            break
        result[M - 1] = 1

    return result


def poisson(lambda_):
    """Get a poisson distributed random number.

    The inverse transform method and the recursive definition are aplied to
    obtain this algorithm.
    """
    U = random()
    i = 0
    F = p = exp(-lambda_)  # Base case

    while U >= F:
        p = p * lambda_ / (i + 1)  # Inductive case
        F += p
        i += 1

    return i

def poisson_acum(lam, j):
    """
    Probabilidad acumulada de la Poisson para int(lambda)
    """
    prob = exp(- lam)
    F = prob
    for i in range(1, j + 1):
        prob *= (lam / i)
        F += prob
    return prob, F


def poisson_optimized(lam):
    """
    Función de distribucion de probabilidad de Poisson optimizada.
    """
    value = int(lam)
    # Calculamos la F(I)
    prob, F = poisson_acum(lam, value)
    u = random()
    if u >= F:
        # Generar X haciendo búsqueda ascendente
        while u >= F:
            value += 1
            prob *= lam / value
            F += prob
        return value - 1  # Devuelve el valor anterior
    else:
        # Generar X haciendo búsqueda descendente
        while u < F:
            F -= prob
            prob *= value / lam
            value -= 1
        return value  # Ejecuta hasta el valor a generar


def random_binomial(n, p):
    """Get a random number with binomial distribution.

    The inverse transform method and the recursive definition are aplied to
    obtain this algorithm.
    """

    U = random()
    i = 0
    F = prob = (1-p)**n  # Base case

    while U >= F:
        prob = (p / (1-p)) * (n-i) / (i+1) * prob  # Inductive case
        F += prob
        i += 1
    return i


if __name__ == '__main__':
    def mean(g, N=10000):
        return sum([g() for _ in range(N)]) / N

    print("\nUniform U(0, 10)")
    print(mean(lambda: uniform_discrete(0, 10)))

    print("\nrandom_geometric(0.5) mean:")
    print(mean(lambda: random_geometric(0.5)))

    print("\nbernoulli mean 0.5:")
    print(mean(lambda: random_bernoulli(0.5)))

    print("\nbernoulli batch 0.8:")
    xs = random_bernoulli_batch(0.8, 1000)
    print(sum(xs) / len(xs))

    print('\npoisson mean 312')
    print(mean(lambda: poisson(312)))

    print('\npoisson optimized mean 312')
    print(mean(lambda: poisson_optimized(312)))

    print('\nBinomial ')
    print(mean(lambda: random_binomial(100, 0.7)))
