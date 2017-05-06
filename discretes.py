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

