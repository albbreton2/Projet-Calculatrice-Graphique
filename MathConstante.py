import numpy as np

#pour les constantes du genre infini, pi, e, etc
# ex: pi = MathConstante("pi")
#input de print(pi) -> pi (faudra ajouter les symboles fancy comme π éventuellement)
#input de pi.operation() -> 3.141592653589793
class MathConstante:
    def __init__(self, nom):
        self.nom = nom
    def __str__(self):
        return self.nom
    def operation(self):
        result = getattr(np, self.nom)
        return result

#hérite de MathConstante, sert pour les fonctions sinusoïdales, exponentielles, logarithmes, etc
#ex: sin = MathFonction("sin")
#input de print(sin) -> sin
#input de sin.operation(x) si x = 1 -> 0.8414709848078965
class MathFonction(MathConstante):
    def __init__(self, nom):
        MathConstante.__init__(self, nom)
    def operation(self, x):
        result = getattr(np, self.nom)
        return result(x)