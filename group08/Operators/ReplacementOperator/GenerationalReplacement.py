from group08.Operators.ReplacementOperator import ReplacementOperator


class GenerationalReplacement(ReplacementOperator.ReplacementOperator):

    def __init__(self):
        super().__init__()  # Constructor de la clase (no tiene efecto).

    # Funcion apply, recibe dos poblaciones, una actual y una nueva, y devuelve la nueva (intercambio generacional)
    def apply(self, populationActual, populationNueva):
        return populationNueva
