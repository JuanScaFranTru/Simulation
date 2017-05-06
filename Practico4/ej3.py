from random import random

def udiscreta(a, b):
    u = random()
    return int(u * (b - a + 1)) + a

def experiment():
    """
    Se lanzan simultáneamente un par de dados legales y se anota el resultado
    de la suma de ambos. El proceso se repite hasta que todos los resultados
    posibles: 2,3,...,12 hayan aparecido al menos una vez.
    """
    # Usamos un set para guardar los resultados
    throws = set()
    iterations = 0
    while len(throws) != 11:
        # Tiramos los dados. Los valores se distribuyen de manera uniforme en
        # el intervalo [1,6] (los valores posible de un dado)
        die1 = udiscreta(1, 6)
        die2 = udiscreta(1, 6)
        # Agregamos el resultado de la suma del lanzamiento
        throws.add(die1 + die2)
        # Una iteración más ha ocurrido
        iterations += 1

    return iterations

def ej3(n):

    for i in range(4):
        prob1 = 0
        prob2 = 0
        for j in range(n):
            prob1 += experiment()
            prob2 += experiment() ** 2
        mean = prob1 / n
        mean2 = prob2 / n
        sigma = (mean2 - mean ** 2) ** (1/2)
        print("N = ", n, "Media = ", mean, "Desviación estandar =", sigma)
        n = n * 10
        
ej3(100)
