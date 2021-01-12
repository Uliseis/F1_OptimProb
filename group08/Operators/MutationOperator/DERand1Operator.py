from group08.Operators.MutationOperator import MutationOperator
from group08.Genome import Genome


class DERand1Operator (MutationOperator.MutationOperator):

    def __init__(self):
        super().__init__()

    '''Se coge la lista de los 3 genomas donor y se aplica 
    la funcion del operador de mutacion de/rand/1 para
    conseguir como resultado el genoma mutado'''
    def apply(self, genomas):
        F = 1.25
        donors = genomas[2]
        res = list()
        for i in range(len(donors[0].solucion)):
            res.append(donors[0].solucion[i] + F * (donors[1].solucion[i] - donors[2].solucion[i]))
        return Genome.Genome(res, 0)

