from random import uniform


def N():
    sum_U = uniform(0, 1)
    niter = 0
    while sum_U <= 1:
        niter += 1
        sum_U += uniform(0, 1)
    return niter


def mean_estimation(nsimulation):
    mean = 0
    var = 0
    for data_len in range(1, nsimulation + 1):
        X = N()
        old_mean = mean
        mean += (X - mean) / data_len
        if var != 0:
            var *= 1 - 1 / (data_len - 1)
        var += data_len * (mean - old_mean)
        # Or (is much better the aproximation, tradeoff with time)
        # var += float(data_len * (mean - old_mean)) ** 2
    return (mean, var, data_len)


def simulation():
    n = 1000

    mean, var, data_len = mean_estimation(n)

    print("Mean = ", mean, "\nVariance = ", var, "\nStd Desv = ", var ** (1/2),
          "\nGenerated Values = ", data_len)


simulation()
