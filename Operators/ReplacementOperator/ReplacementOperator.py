from abc import ABC, abstractmethod

class ReplacementOperator (ABC):
    @abstractmethod
    def __init__(self):  # Constructor de la clase abstracta (no tiene efecto).
        pass

    # Metodo abstracto para el operador de reemplazo
    @abstractmethod
    def apply (self,population1, population2):
        pass