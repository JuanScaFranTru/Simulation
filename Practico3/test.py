import random
from math import exp, log, factorial
# Poisson probability method
def poisson(lamb, s):
    ret = exp(-(lamb)) * (lamb ** s) / factorial(s)
    return ret

eja = poisson(3 + (4*log(2)), 5)
print("Ejerc 6)a): ", eja)

ejb = poisson(6 + (4*log(3)), 8)
print("\nEjerc 6)b): ", ejb)

ejbb = poisson(3 + (4*log(3)) - (4*log(2)), 3)
print("\nEjerc 6)bb): ", ejbb)

bla = 3 + (4*log(3)) - (4*log(2))
print("\n", bla)
