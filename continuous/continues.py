from random import random
from math import exp, log, pi, sqrt, sin, cos


def inverse_transform_nroot(n):
    return random() ** (1/n)


def reject_nroot(n):
    """
    Si se desea simular una va con distribución Fx(x) = x**n, en lugar de tomar
    una raíz n-ésima es conveniente generar n uniformes y tomar su máximo.
    """
    maxm = max([random() for _ in range(n)])
    return maxm


def another_nroot(n):
    Y = random()
    U = random()
    while U >= Y**(n-1):
        U = random()
        Y = random()
    return Y


def exponential(lam):
    """
    Simulación de una va Exponencial con parámetro Lambda
    Dado que u ~ U(0,1) entonces (1 - u) ~ U(0,1)
    """
    U = random()
    return (- log(U)) / lam


def poisson_proc1(lam):
    n = 0
    prod = random()
    bound = exp(- lam)
    while prod < bound:
        n += 1
        prod += random()
    return n - 1


def gamma(n, lam):
    """
    Una suma de n variables aleatorias exponenciales, independientes, con
    parámetro lambda es una va X ~ Gamma(m, lambda).
    """
    U = 1
    for _ in range(n):
        U *= random()
        return (- log(U)) / lam


def twoExponential(lam):
    """
    Se utiliza el siguiente teorema:

        Si X,Y ~ e(lambda), independientes, entonces
            X es condiconal a X + Y = t es uniforme en (0, t)
    """
    t = (-1 / lam) * log(random() * random())  # Valor de una Gamma(2, lambda)
    X = t * random()
    Y = t - X
    return (X, Y)


def nExponentials(lam, n):
    """
    Para generar n exponenciales a partir de una X ~ Gamm(n, lambda) se
    requiere calcular un único logaritmo y n - 1 uniformes adicionales:
    V_1,..., V_(n-1).
    En primer lugar se ordenan los valores de las Vi:
                V_i_1 < ... < V_i_(n-1)
    Si X = t, entonces el intervalo (0,t) se divide en n subintervalos no
    superpuestos, de longitud:
                t*V_i_q, ..., t * (V_i_(n-1) - V_i_(n-2)), t * (1 - V_i_(n-1))
    """
    Us = [random() for _ in range(n)]
    X = sum([log(u) for u in Us])
    t = (- 1 / lam) * X

    Vs = [random() for _ in range(n - 1)]

    Vs.sort()
    result = [t * (Vs[i] - Vs[i - 1]) for i in range(1, n - 2)]
    return [t * Vs[0]] + result + [t - t * Vs[n - 2]]


def normal(mu, sigma):
    """
    Si queremos generar una X ~ N(mu, sigma), podemos deciel que si
    Z ~ N(0,1), entonces:

                    X = sigma * Z + mu ~ N(mu, sigma)

    Como la funcion de dencidad de Z es par, se puede generar |Z| y luego usar
    un método de composición:

                    Fz(x) = 0.5 * F_|z|(x) + 0.5 * F_(-|z|)(x)

    Se utiliza el método de rechazo con una exponencial para generar Z.
    """
    Y1 = -log(random())
    Y2 = - log(random())
    while Y2 < ((Y1 - 1) ** 2) / 2:
        # Generamos la Z
        Y1 = -log(random())
        Y2 = - log(random())
    # usamos la Z para calcular la Normal con el método de composición
    if random() < 0.5:
        return Y1 * sigma + mu
    else:
        return - Y1 * sigma + mu


def stdnormal_polar():
    """
    Genera dos variables normales estándar.
    """
    rcuad = - 2 * log(random())
    theta = 2 * pi * random()
    x = sqrt(rcuad) * cos(theta)
    y = sqrt(rcuad) * sin(theta)
    return (x, y)


def polar_optimized():
    """
    Optimized Box Muller transform used
    """
    while True:
        V1, V2 = 2 * random() - 1, 2 * random() - 1
        S = V1 ** 2 + V2 ** 2
        if S <= 1:
            break
    X = V1 * sqrt(-2 * log(S) / S)
    Y = V2 * sqrt(-2 * log(S) / S)
    return (X, Y)


a = [list(polar_optimized()) for i in range(1000000)]
b = []
for i in a:
    b += i
print(sum(b) / 1000000)
