import numpy as np

matriz = np.zeros((5, 5))   # Crear matriz 5 x 5 llena de ceros

# Posición central
fila = 2
columna = 2
matriz[fila, columna] = 1    # Colocar un 1 en el centro

# Mostrar matriz
print(f"Matriz:\n{matriz}")

# Mostrar vecinos
print("\nVecinos:")

# Recorrer posiciones alrededor del centro
for i in range(fila - 1, fila + 2):
    for j in range(columna - 1, columna + 2):

        # Evitar imprimir la celda central
        if i == fila and j == columna:
            continue

        print(f"Vecino en ({i}, {j}) = {matriz[i, j]}")