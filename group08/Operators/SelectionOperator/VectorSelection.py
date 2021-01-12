from group08.Operators.SelectionOperator import SelectionOperator
import random as rd


class VectorSelection(SelectionOperator.SelectionOperator):

    def __init__(self):  # Constructor de la clase (no tiene efecto).
        super().__init__()

    '''Se selecciona el genoma de la posicion i como target y se 
     seleccionan posteriormente los 3 genomas donor que no podran
     coincidir con el target ni podran repetirse entre ellos.
     Se devuelve una lista de 4 genomas: 1 target y 3 donor'''
    def apply(self, genomes, i):
        target = genomes[i]
        vectors = list()
        vectors.append(target)
        for j in range(3):
            while True:
                pos = rd.randint(0, i)
                donoraux = genomes[pos]
                for k in range(len(vectors)):
                    if donoraux == vectors[k]:
                        continue
                vectors.append(donoraux)
                break
        return vectors


