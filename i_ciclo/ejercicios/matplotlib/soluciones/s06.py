import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Se define la cantidad de filas y columnas
filas = 20
columnas = 20

# 99% sanos y 1% infectados
matriz = np.random.choice([0, 1], size=(filas, columnas), p=[0.99, 0.01])

# Colores:
# Sano: Azul
# Infectado: Rojo
# Recuperado: Verde
colores = ListedColormap(["blue", "red", "green"])

# Se van a ejecutar solo 15 pasos
for paso in range(15):
    nueva = matriz.copy()       # Se copia la matriz original para generar el siguiente paso en la simulación

    # Recorrer posiciones internas
    for i in range(1, filas - 1):
        for j in range(1, columnas - 1):

            # Persona sana depende de los vecinos
            if matriz[i, j] == 0:

                # Revisar vecinos
                if (matriz[i-1, j] == 1 or matriz[i+1, j] == 1 or matriz[i, j-1] == 1 or matriz[i, j+1] == 1):
                    nueva[i, j] = 1

            # Infectado se recupera
            elif matriz[i, j] == 1:
                nueva[i, j] = 2

    matriz = nueva  # Se intercambian las matrices

    # Se muestran los datos
    plt.imshow(matriz, cmap=colores, vmin=0, vmax=3)
    plt.title(f"Paso {paso}")
    plt.show()

    # Al usar un ciclo for, paso incrementa automáticamente