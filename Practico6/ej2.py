from random import random
from math import exp, sqrt


def mean_estimation(min_simlation, accept_value):
    mean = 0
    var = 0
    data_len = 0
    while data_len < min_simlation or var > accept_value:
        # Or (is much better the aproximation, tradeoff with time)
        # wile data_len < min_simlation or sqrt(var / data_len) > accept_value:
        data_len += 1
        X = exp(random() ** 2)
        old_mean = mean
        mean += (X - mean) / data_len
        if var != 0:
            var *= 1 - 1 / (data_len - 1)
        var += data_len * (mean - old_mean)
        # Or (is much better the aproximation, tradeoff with time)
        # var += float(data_len * (mean - old_mean)) ** 2

    return (mean, var, data_len)


def simulation():
    n = 100
    acceptable_value = 0.01 ** 2  # Std Desviation ** 2 == var

    mean, var, data_len = mean_estimation(n, acceptable_value)

    print("Mean = ", mean, "\nVariance = ", var, "\nStd Desv = ", var ** (1/2),
          "\nGenerated Values = ", data_len)


simulation()
