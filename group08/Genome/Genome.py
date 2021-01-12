class Genome:
    #Genoma
    solucion = list()
    #Fitness del genoma
    fitness = 0

    def __init__(self, solucion, fitness):
        self.solucion = solucion
        self.fitness = fitness

    def getSolucion(self):
        return self.solucion

    def getFitness(self):
        return self.fitness

    #El fitness del genoma pasa a ser "fit"
    def setFitness(self, fit):
        self.fitness = fit

