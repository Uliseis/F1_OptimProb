import math

from group08.Genome.Genome import Genome
from group08.Population.Population import Population
from group08.Operators.CrossoverOperator import BinomialCrossoverOperator
from group08.Operators.MutationOperator import DERand1Operator
from group08.Operators.SelectionOperator import VectorSelection
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
		self.crossOper = BinomialCrossoverOperator.BinomialCrossoverOperator()
		self.mutOper = DERand1Operator.DERand1Operator()
		self.replOper = GenerationalReplacement.GenerationalReplacement()
		self.selecOper = VectorSelection.VectorSelection()
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
		for i in range(0, popul.psize):
			#Seleccionamos cuatreo genomas de la poblacion actual: el target y tres random
			selected = self.selecOper.apply(popul, i)
			targetVector = selected[0]
			donors = list()
			donors.append(selected[1])
			donors.append(selected[2])
			donors.append(selected[3])
			#Obtenemos el genoma mutado
			bestGenome = popul.bestFitness()
			mutationParam = [targetVector, bestGenome, donors]
			mutationVector = self.mutOper.apply(mutationParam)
			#Aplicamos el CrossoverOperator entre el targetVector y el mutationVector
			crossed = self.crossOper.apply([targetVector, mutationVector])
			crossed[0].fitness = self.calcular_fitness(crossed[0].getSolucion())
			#Incluimos el nuevo individuo en la  poblacion
			newpopulation.add(crossed[0])

		self.colocLimites(newpopulation)
		#Se obtiene a la nueva poblacion de forma elitista
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

