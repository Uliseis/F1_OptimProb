import math

from group08.Genome.Genome import Genome
from group08.Population.Population import Population
from group08.Operators.CrossoverOperator import TwoPointOperator
from group08.Operators.MutationOperator import GaussianOperator
from group08.Operators.SelectionOperator import TournamentSelection
from group08.Operators.ReplacementOperator import GenerationalReplacement

import numpy as np
import random

class EA(object):
	"""docstring for EA"""
	bounds = list ()
	psize = 0
	population = Population(0)
	crossOper = None
	mutOper = None
	replOper = None
	selecOper = None
	minfun = None

	#Constructor de la clase EA. Inicializa la poblacion y los operadores
	def __init__(self, minfun, bounds, psize):
		super(EA, self).__init__()
		self.minfun = minfun
		self.bounds = bounds
		self.psize = psize
		self.population = Population(len(bounds))
		self.crossOper = TwoPointOperator.TwoPointOperator()
		self.mutOper = GaussianOperator.GaussianOperator()
		self.replOper = GenerationalReplacement.GenerationalReplacement()
		self.selecOper = TournamentSelection.TournamentSelection()
		self.population = self.initpopulation()

	#Metodo que corre el algoritmo genetico num veces
	def run(self,num):
		for i in range(num):
			self.population = self.algorithm(self.population) #Cambia la poblacion en cada iteracion(generacion)

	#Algoritmo. Recibe la poblacion actual
	def algorithm(self, popul):
		#Se crea una nueva poblacion que sera la siguiente
		newpopulation = Population(self.psize)
		#Se realiza el bucle para cada dos individuos
		for i in range(0, math.floor(self.psize/2)):
			#Seleccionamos dos genomas de la poblacion actual
			selected = [self.selecOper.apply(popul, 0)[0], self.selecOper.apply(popul, 0)[0]]
			#Les aplicamos el crossover operator
			crossed = self.crossOper.apply(selected)
			crossed[0].fitness = self.calcular_fitness(crossed[0].getSolucion())
			crossed[1].fitness = self.calcular_fitness(crossed[1].getSolucion())
			#Mutamos a los nuevos individuos
			gen1 = self.mutOper.apply([crossed[0]])
			gen1.fitness = self.calcular_fitness(gen1.getSolucion())
			gen2 = self.mutOper.apply([crossed[1]])
			gen2.fitness = self.calcular_fitness(gen2.getSolucion())
			#Incluimos los nuevos individuos en la nueva poblacion
			newpopulation.add(gen1)
			newpopulation.add(gen2)

		self.colocLimites(newpopulation)
		#La nueva poblacion se convierte en la poblacion actual a traves del remplazo generacional
		return self.replOper.apply(popul, newpopulation)

	#Inicia las variables de cada genoma aleatoriamente y añade psize genomas a la poblacion
	def initpopulation(self):
		p = Population(self.psize);
		for i in range(self.psize):
			listaVariables = list()
			for j in range(len(self.bounds)):
				listaVariables.append(random.uniform(self.bounds[j][0], self.bounds[j][1]))
			gen = Genome(listaVariables, self.calcular_fitness(listaVariables))
			p.add(gen)
		return p

	#Metodo que recoloca cada variable de los genomas de la poblacion si se han salido
	#de los limites con los que se ha creado EA
	def colocLimites(self, pop):
		for i in range(self.psize):
			for j in range(len(self.bounds)):
				if pop.population[i].solucion[j] < self.bounds[j][0]:
					pop.population[i].solucion[j] = self.bounds[j][0]
				elif pop.population[i].solucion[j] > self.bounds[j][1]:
					pop.population[i].solucion[j] = self.bounds[j][1]

	#Metodo que calcula el fitness de un genoma en funcion del valor que se obtiene con minfun
	def calcular_fitness(self, variables):
		return self.minfun(variables)

	#Metodo que devuelve el mejor genoma de una poblacion
	def best(self):
		return self.population.bestFitness()

