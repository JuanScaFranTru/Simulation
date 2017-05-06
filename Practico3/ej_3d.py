import random
from math import exp, log, factorial

# Function used to apply Monte Carlo
def g(x, y):
    ret = exp((x + y)**2)

    return ret

# Initilize the num of iterations
n = 100

for j in range(5):
    est = 0
    for i in range(n):
        # compute the value of g(u_i) and cumulate in 'est'
        est = est + g(random.uniform(0, 1), random.uniform(0, 1))
    # Divide by the number of iterations (number of u_i) to obtain the E[g(U)]
    est = est / n
    print("N = ", n, ", O = ", est, "\n")
    # Invariant: n**j
    n = n * 10
