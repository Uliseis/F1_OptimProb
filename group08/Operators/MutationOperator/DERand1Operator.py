from group08.Operators.MutationOperator import MutationOperator
from group08.Genome import Genome


class DERand1Operator (MutationOperator.MutationOperator):

    global F

    def __init__(self):
        super().__init__()
        F = 1.2567

    '''Se coge la lista de los 3 genomas donor y se aplica 
    la funcion del operador de mutacion de/rand/1 para
    conseguir como resultado el genoma mutado'''
    def apply(self, genomas):
        donors = genomas[2]
        res = list()
        for i in range(len(donors[0])):
            res.append(donors[i] + F * (donors[i] - donors[i]))
        return res

