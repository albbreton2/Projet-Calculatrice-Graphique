import numpy as np
import matplotlib.pyplot as plt

def tracer_graphique(fonctions, x_min=-10, x_max=10):
    x = np.linspace(x_min, x_max, 500)

    plt.figure(figsize=(10, 6))

    operations = {
        "x": x,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "sqrt": np.sqrt,
        "cbrt": np.cbrt,
        "log": np.log,
        "log10": np.log10,
        "log2": np.log2,
        "exp": np.exp,
        "abs": np.abs,
        "floor": np.floor,
        "ceil": np.ceil,
        "pi": np.pi,
        "e": np.e
    }

    for fonction in fonctions:
        try:
            expression = fonction.replace("^", "**")
            y = eval(expression, {"__builtins__": {}}, operations)

            if np.isscalar(y):
                y = np.full_like(x, y)

            plt.plot(x, y, label=fonction)

        except (ValueError, TypeError, SyntaxError, NameError, ZeroDivisionError):
            print("Erreur dans la fonction :", fonction)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graphique de la fonction")
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.grid(True)
    plt.xlim(x_min, x_max)
    plt.legend()
    plt.show()

