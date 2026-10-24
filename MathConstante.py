import numpy as np

#pour les constantes du genre infini, pi, e, etc
# ex: pi = MathConstante("pi")
#input de print(pi) -> π
#ce que pi.operation fait -> np.pi()
#input de pi.operation() -> 3.141592653589793
class MathConstante:
    def __init__(self, nom):
        self.nom = nom
        self.symboles = {
            "pi" : "π", 
            "inf" : "∞", 
            "sqrt" : "√", 
            "cbrt" : "∛", 
            "floor" : "⌈ ⌉", 
            "ceil" : "⌊ ⌋", 
            "exp" : "eˣ",
            "log" : "ln",
            "log10" : "log₁₀",
            "log2" : "log₂",
            "absolute" : "| |"
            }

    def __str__(self):
        if self.nom in self.symboles:
            return self.symboles[self.nom]
        else:
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