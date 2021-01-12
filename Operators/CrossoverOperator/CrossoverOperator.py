from abc import ABC, abstractmethod

class CrossoverOperator(ABC):
    
    @abstractmethod  # Constructor de la clase abstracta (no tiene efecto).
    def __init__(self):
        pass

    # Metodo abstracto para el operador de cruce
    @abstractmethod
    def apply(self, genomas):
        pass
