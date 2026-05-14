import numpy as np

notas = np.array([68, 72, 100, 90, 55, 83, 79, 61])

corregidas = notas + 5

mayores = np.where(corregidas > 100)
corregidas[mayores] = 100

print(f"Notas corregidas: {corregidas}")
print(f"Cantidad de aprobados: {corregidas.size}")