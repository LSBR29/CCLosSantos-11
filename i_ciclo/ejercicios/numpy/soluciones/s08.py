import numpy as np

lanzamientos = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0])

cantidadCaras = lanzamientos[lanzamientos == 1].size
nuevo = np.where(lanzamientos == 1, "Cara", "Escudo")

print(f"Cantidad de caras: {cantidadCaras}")
print(f"Resultado del lanzamiento:\n{nuevo}")