from group08.Operators.ReplacementOperator import ReplacementOperator
from group08.Population.Population import Population


class GenerationalReplacement(ReplacementOperator.ReplacementOperator):

    def __init__(self):
        super().__init__()

    '''El metodo contruye una poblacion con los mejores genomas de la poblacionActual y de la poblacioNueva. '''

    def apply(self, populationActual, populationNueva):
        size = populationActual.psize
        population = Population(size)
        for i in range(size):
            if populationActual.population[i].getFitness() >= populationNueva.population[i].getFitness():
                population.add(populationActual.population[i])
            else:
                population.add(populationNueva.population[i])
        return population
