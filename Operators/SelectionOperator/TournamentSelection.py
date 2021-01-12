from group08.Operators.SelectionOperator import SelectionOperator
import numpy as np
import random as rd


class TournamentSelection(SelectionOperator.SelectionOperator):
    k = 0

    def __init__(self):
        super().__init__()
        self.k = 2

    #Selecciona de forma aleatoria k genomas de la poblacion
    def select(self, genomes):
        selected = list()
        while len(selected) < self.k:
            random = rd.randint(0, len(genomes) - 1)
            if genomes[random] not in selected:
                selected.append(genomes[random])
        return selected

    @staticmethod
    def total(selected):  #Fitness total
        total = 0
        for i in selected:
            total += i.fitness
        return total

    '''A los genomas seleccionados se les asigna una probabilidad ,p1, 
     en función de su fitness, una vez la tienen asignada se compara 
     con una probabilidad aleatoria,rand, de manera que si p1 >= rand el
     genoma con probabildad p1 es seleccionado'''
    def apply(self, genomes, num):
        p = self.select(genomes.population)
        total = self.total(p)
        props = [None] * self.k
        for i in range(self.k):
            props[i] = (total - p[i].fitness) / total
            rand = np.random.rand()
            if rand <= props[i]:
                return [p[i]]

        return [p[self.k - 1]]



