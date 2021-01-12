from abc import ABC, abstractmethod

class SelectionOperator (ABC):
    @abstractmethod
    def __init__ (self):
        pass

    @abstractmethod
    def apply (self, genomes, num):
        pass