from group08.Operators.CrossoverOperator import CrossoverOperator
from group08.Genome.Genome import Genome
import numpy as np
import random


class BinomialCrossoverOperator(CrossoverOperator.CrossoverOperator):

    def __init__(self):
        super().__init__()

    ''' El parametro genomas_list es una lista de 2 genomas, target_vector y mutant vector.
        El metodo contruye un vector a partir de estos vectores. Se genera un numero,rand, que sigue
        una distribucion Uniforme[0,1]. El vector se va creando con valores del target_vector o del 
        mutant_vector en funcion del valor rand con CR. '''

    def apply(self, genomas_list):
        CR = 0.5
        trial_vector = []
        target_vector = genomas_list[0]
        mutant_vector = genomas_list[1]
        rand = np.random.uniform(0, 1, None)
        size = len(target_vector.getSolucion())
        irand = random.randint(1, size)
        for i in range(size):
            if rand <= CR or i == irand:
                trial_vector.append(mutant_vector[i])
            else:
                trial_vector.append(target_vector[i])
        trial_genome = Genome(trial_vector, 0)
        return [trial_genome]
