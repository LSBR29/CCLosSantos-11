import numpy as np
import matplotlib.pyplot as plt

# Se define la cantidad de filas y columnas
filas = 15
columnas = 15

# Con np.zeros((tamaño)) se puede crear una matriz llena de 0s
matriz = np.zeros((filas, columnas))
matriz[7, 7] = 100      # En el centro se coloca un 100

tiempo = 0      # Se usará un ciclo while con contador para ir "avanzando"
while tiempo <= 10:
    nueva = matriz.copy()       # Se copia la matriz original para generar el siguiente paso en la simulación

    # Recorrer posiciones internas
    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            # Promedio de cada celda en la matriz nueva usando los datos originales
            nueva[i, j] = (matriz[i, j] + matriz[i-1, j] + matriz[i+1, j] + matriz[i, j-1] + matriz[i, j+1]) / 5

    matriz = nueva  # Se intercambian las matrices

    # Se muestran los datos
    plt.imshow(nueva, cmap="hot")
    plt.title(f"Tiempo = {tiempo}s")
    plt.show()

    tiempo += 1     # Se incrementa el tiempo