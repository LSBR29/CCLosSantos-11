import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 100, 10)   # Generar una lista de 10 aleatorios entre 1 y 100
y = np.random.randint(1, 100, 10)

plt.scatter(x, y, facecolors="none", edgecolors="b")    # Quita el fondo y hace el borde azul
plt.show()