from abc import ABC, abstractmethod

class MutationOperator (ABC):
    @abstractmethod  # Constructor de la clase abstracta (no tiene efecto).
    def __init__(self):
        pass

    # Metodo abstracto para el operador de mutacion
    @abstractmethod
    def apply(self, genomes):
        pass