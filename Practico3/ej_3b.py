import random

# Function used to apply Monte Carlo
def g(u):
    ret = (1 / u - 1) * ((u**2) / ((1 - 2 * u + 2 * u**2)**2))
    return ret

# Initilize the num of iterations

n = 100
for j in range(5):
    est = 0
    for i in range(n):
        # Generate a random nomber between 0 and 1
        rand = random.uniform(0, 1)
        # compute the value of g(u_i) and cumulate in 'est'
        est = est + g(rand)
    # Divide by the number of iterations (number of u_i) to obtain the E[g(U)]
    est = est / n
    print("N = ", n, ", O = ", est, "\n")
    # Invariant: n**j
    n = n * 10
