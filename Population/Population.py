
class Population:
    population = None #Lista con los genemos
    psize = 0   #Tamaño de la lista

    def __init__(self, psize):
        self.psize = psize
        self.population = list()

    #Añade un genoma,genome, a la poblacion
    def add(self, genome):
        if len(self.population) < self.psize:
            self.population.append(genome)
        else:
            return -1
        return 0
    #Elimina un determinado genoma,toremove, de la poblacion
    def remove(self, toremove):
        if len(self.population) > 1:
            self.population.remove(toremove)
    '''Devuelve una poblacion ordenada en funcion de los fitness de los genomas que lo componen.
     Es ascendente, por defecto, o descendiente ,si se le llama con reverse = True como parametro,'''
    def sort(self, reverse=False):
        if not reverse:
            for i in range(self.psize):
                for j in range(i + 1, self.psize):
                    if self.population[i].getFitness() < self.population[j].getFitness():
                        self.population[i], self.population[j] = self.population[j], self.population[i]
        else:
            for i in range(self.psize):
                for j in range(i + 1, self.psize):
                    if self.population[i].getFitness() > self.population[j].getFitness():
                        self.population[i], self.population[j] = self.population[j], self.population[i]

        return self.population

    #Devuelve el genoma con el mejor fitness
    def bestFitness(self):
        return self.sort(reverse=True)[0]

    '''Reemplaza un genoma antiguo por uno nuevo y 
    devuelve so posicion en la poblacion'''
    def replaceSol(self, oldsol, newsol):
        i = self.population.index(oldsol)
        self.population[i] = newsol
        return i

    #Devuelve el sumatorio del fitness de cada genoma de la poblacion
    def getTotalFitness(self):
        total = 0
        for i in range(self.psize):
            total += self.population[i].getFitness()
        return total

    #Devuelve el fitness medio de la poblacion
    def getAverageFitness(self):
        return self.getTotalFitness() / self.psize
