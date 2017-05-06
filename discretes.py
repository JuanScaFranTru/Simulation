from random import random
from math import log
from math import exp


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


def uniform_discrete_not_simplified(n):
    """Discrete Uniform distribution.

    Get a random natural number in the interval [1, n].
    """
    U = random()
    F = 1 / n
    x = 1
    while U >= F:
        F += 1/n
        x += 1
    return x


def uniform_discrete_simplified(n):
    """Discrete Uniform distribution.

    Get a random natural number in the interval [1, n]. This is an
    equivalent but more efficient algorithm for discrete uniformly
    distributed random number generation.

    The equivalence can be proven in the following way:

    Given that the algorithm will output j if and only if:

        (j-1)/n <= U(0, 1) <= j/n

    U belongs to [(j-1)/n, j/n) iff n * U belongs to [j-1, j]. But this
    will occur if and only if:

        j = floor(n * U) + 1

    given that int(n * U) is the same as floor(n * U), we obtain:

        j = int(n * U) + 1

    """
    U = random()
    return int(n * U) + 1


def uniform_discrete(m, k):
    """Discrete Uniform distribution.

    Get a random natural number in the interval [m, k].
    """
    U = random()
    return int(U * (k - m + 1)) + m


def random_permutation(x):
    """Get an equiprobable random permutation of x."""
    N = len(x)
    for j in reversed(range(N)):
        # Generate a random number in the interval [1, j]
        i = int(j * random())

        # Swap values
        x[j], x[i] = x[i], x[j]
    return x


def random_subset(r, A):
    """Get an equiprobable random subset of A with r elements.

    Basically, the key observation of this algorithm is that a subset of a
    random permutation is the same as a random subset. Thus, using the
    previous algorithm a random subset can be obtained.

    :param r: number of elements in the generated subset
    :param A: set (represented as a list)

    """
    N = len(A)
    for j in reversed(range(N - r, N)):  # Note the change in the range
        i = int(j * random())
        A[j], A[i] = A[i], A[j]
    return A[:r]  # Return the subset


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
