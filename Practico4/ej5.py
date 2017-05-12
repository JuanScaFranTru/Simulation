from random import random


def my_dist(j):
    """
    Funcion de distribucion de probabilidad dada en el ejercicio
    """
    prob = 0
    if j >= 1:
        prob = (1/2)**(j+1) + ((1/2) * 2**(j-1)) / 3**j
    return prob


def acum(k):
    """
    Funcion de Distribución acumulada hasta el valor k.
    """
    prob = 0
    for i in range(1, k):
        prob += my_dist(i)
    return prob


def ej5():
    """
    Generamos la Variable aleatoria con distribución de probabilidad dada por
    my_dist. Usando el metodo de la Transformada inversa
    """
    u = random()
    i = 1
    F = my_dist(i)
    while u >= F:
        i += 1
        F += acum(i)
    return i


vas = set([ej5() for i in range(100)])
print(vas)
