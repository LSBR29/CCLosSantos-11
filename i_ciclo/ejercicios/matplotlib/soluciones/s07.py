import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

filas = 10
columnas = 10
matriz = np.array([
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,0,1,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
])

# Punto inicial
matriz[1,1] = 2

# Colores:
# Vacío: Blanco
# Pared: Negro
# Relleno: Azul
colores = ListedColormap(["white", "black", "blue"])

paso = 0
while True:
    nueva = matriz.copy()       # Se copia la matriz original para generar el siguiente paso en la simulación

    # Recorrer posiciones internas
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):

            # Celda vacía depende de los vecinos
            if matriz[i, j] == 0:

                # Revisar vecinos
                if (matriz[i-1, j] == 2 or matriz[i+1, j] == 2 or matriz[i, j-1] == 2 or matriz[i, j+1] == 2):
                    nueva[i, j] = 2

    # Si no hubo cambios, terminar
    if np.array_equal(matriz, nueva):
        break

    matriz = nueva  # Se intercambian las matrices

    # Se muestran los datos
    plt.imshow(matriz, cmap=colores, vmin=0, vmax=2)
    plt.title(f"Paso {paso}")
    plt.show()

    paso += 1   # Se incrementa el número de pasos

plt.imshow(matriz, cmap=colores, vmin=0, vmax=2)
plt.title(f"Resultado")
plt.show()