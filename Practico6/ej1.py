from random import uniform
from math import sqrt, log


def twonormal2(mu, sigma):
    """Return two normal distributed random variables."""
    while True:
        U1, U2 = uniform(-1, 1), uniform(-1, 1)
        S = U1 ** 2 + U2 ** 2
        if S <= 1:
            break

    tmp = sqrt(-2 * log(S) / S)
    return U1 * tmp, U2 * tmp


def mean_estimation(min_simlation, accept_value):
    mean = 0
    var = 0
    data_len = 0
    while data_len < min_simlation or (var / data_len) ** (1/2) > accept_value:
        data_len += 1
        X, _ = twonormal2(0, 1)
        old_mean = mean
        mean += 1 / data_len * (X - mean)
        if var != 0:
            var *= (1 - 1 / (data_len - 1))
        var += data_len * (mean - old_mean)**2
    return (mean, var, data_len)


def simulation():
    n = 30
    acceptable_value = 0.1

    mean, var, data_len = mean_estimation(n, acceptable_value)

    print("Mean = ", mean, "\nVariance = ", var, "\nStd Desv = ", var ** (1/2),
          "\nGenerated Values = ", data_len)


simulation()
