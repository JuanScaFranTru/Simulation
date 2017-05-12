from random import random
from pynverse import inversefunc


def inverse_transform(F):
    """
    Se utiliza la propoción que dice:
        Sea U ~ U(0,1) una variable aleatoria. Para cualquier distribución
        continua F, monótona creciente en F**(-1), la va X definida por:
            X = F**(-1)
        Tiene distribución F.
    """
    U = random()
    G = inversefunc(F)
    return G(U)  # G = F ** (-1)
