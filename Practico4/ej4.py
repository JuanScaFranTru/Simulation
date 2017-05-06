from random import random
from math import exp, log, factorial


def poisson_acum(lam, j):
    """
    Probabilidad acumulada de la Poisson para int(lambda)
    """
#    print("Calculando la acumulada de ", j)
    prob = exp(- lam)
    F = prob
    for i in range(1, j):
        prob *= (j / i)
        F += prob
#    print("La acumulada es", prob)
    return prob

def Poisson(lam):
    """
    Función de distribucion de probabilidad de Poisson optimizada.
    """
    value = int(lam)
    # Calculamos la F(I)
    F = poisson_acum(lam, value)
    prob = F
    u = random()
    if u >= F:
        print("Haciendo busqueda ascendente")
        # Generar X haciendo búsqueda ascendente
        while u >= F:
            value += 1
            prob *= log(lam / value)
            F += prob
        return value - 1 # Devuelve el valor anterior
    else:
        print("Haciendo busqueda descendente")
        # Generar X haciendo búsqueda descendente
        while u < F:
            F -= prob
            prob *= log(value / lam)
            value -= 1
        return value # Ejecuta hasta el valor a generar

# ----------------- A partir de acá es el ejercicio ------------------------

def my_poisson(lam, k, i):
    acum = poisson_acum(lam, k)
    poisson = (lam ** i / factorial(i)) * exp(- lam)

    return poisson / acum

def my_acum(lam, k, j):
    prob = 0
    for i in range(j):
        prob += my_poisson(lam, k, i)
    return prob

def ej4(lam, k):
    u = random()
    i = 0
    F = my_acum(lam, k, i)
    while u >= F:
        i += 1
        F += my_acum(lam, k, i)
    return i

a = [ej4(2, 10) for i in range(100)]
print(a)
