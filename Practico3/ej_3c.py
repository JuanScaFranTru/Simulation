import random
from math import exp, log, factorial
def g(u):
    return exp(-(1/u - 1)**2) * (1/u)**2
n = 100
for j in range(5):
    est = sum([g(random.uniform(0,1)) for x in range(n)]) / n
    print("N = ", n, ", O = ", 2 * est, "\n")
    n = n * 10
