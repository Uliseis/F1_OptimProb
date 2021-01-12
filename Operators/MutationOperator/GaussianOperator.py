from group08.Operators.MutationOperator import MutationOperator
from group08.Genome import Genome
import numpy as np


class GaussianOperator (MutationOperator.MutationOperator):

    def __init__(self):  # Constructor de la clase (no tiene efecto).
        super().__init__()

    # Funcion apply, recibe una lista de un genoma y devuelve otro con una mutacion gaussiana
    def apply(self, genomas):
        genoma = genomas[0]
        res = genoma.getSolucion()
        sigma = 0.5  # El sigma se escoge de forma que la funcion sea equilibrada
        size = len(genoma.getSolucion())
        for i in range(0, size):
            prob = np.random.rand()  # Se utiliza una probabilidad aleatoria con dominio de 0 a 1
            if prob < 0.15:  # Si la probabilidad es menor que 0.15 se hace la mutacion
                # NP RANDOM NORMAL utiliza una funcion Gaussiana, y mutara el elemento
                res[i] = np.random.normal(genoma.getSolucion()[i], sigma)
        return Genome.Genome(res, 0)


