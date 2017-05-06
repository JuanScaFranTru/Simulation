from random import random


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
