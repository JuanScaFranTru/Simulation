from random import random

def compos(p, F):
    """
    El algoritmo es básicamente:
    - Genero va Discreta I (1...n). Genera el valor j
    - Calculo P(I = j) = alphaj
    - Genero Fj (sé generarla)
    - Ahora hago Fj * alphaj
    - Repito hasta n

    :param p: Arreglo de probabilidades de que I tome el valor i
    :param F: Arreglo de simulaciones de funciones fi cuya distribucion es Fi
              correspondientemente
    """
