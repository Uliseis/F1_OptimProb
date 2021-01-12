from group08.Operators.CrossoverOperator import CrossoverOperator
from group08.Genome import Genome
import numpy as np


class TwoPointOperator(CrossoverOperator.CrossoverOperator):
    def __init__(self):  # Constructor de la clase (no tiene efecto).
        super().__init__()

    # Funcion apply, recibe una lista de dos genomas y devuelve sus dos hijos
    def apply(self, genomas):
        aux1 = list()
        aux2 = list()   # Se crean las dos listas para los hijos
        size = len(genomas[0].getSolucion())
        indexp1 = np.random.randint(0, size / 2)
        indexp2 = np.random.randint(size / 2, size)  # Se determinan dos indices para acotar la zona de los padres

        # El bucle itera sobre las soluciones de los genomas para crear sus hijos
        for i in range(0, size):
            if i < indexp1 or i > indexp2:  # Se añaden la primera y ultima parte del padre correspondiente a cada hijo
                aux1.append(genomas[0].getSolucion()[i])
                aux2.append(genomas[1].getSolucion()[i])
            else:  # Se añade la parte intermedia del padre correspondiente a cada hijo
                aux1.append(genomas[1].getSolucion()[i])
                aux2.append(genomas[0].getSolucion()[i])

        hijo1 = Genome.Genome(aux1, 0)
        hijo2 = Genome.Genome(aux2, 0)
        hijos = [hijo1, hijo2]  # Se crean los hijos, se guardan en una lista y se devuelve la lista
        return hijos
