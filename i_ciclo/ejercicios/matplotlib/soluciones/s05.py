import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap    # Para poner colores personalizados

# Se define la cantidad de filas y columnas
filas = 25
columnas = 25

# Con np.rancom.choice([valores], size=(tamaño), p=[probabilidades]) se pueden crear matrices aleatoria
# 20% vacío y 80% sano
matriz = np.random.choice([0, 1], size=(filas, columnas), p=[0.2, 0.8])
matriz[1, 1] = 2    # En (1, 1) se inicia el fuego

# Colores personalizados
# Suelo vacío: Negro
# Árbol sano: Verde
# Árbol en fuego: Rojo
# Cenizas: Gris
colores = ListedColormap(["black", "green", "red", "gray"])

paso = 0    # Para ir imprimiendo el tiempo actual
while 2 in matriz:
    nueva = matriz.copy()       # Se copia la matriz original para generar el siguiente paso en la simulación

    # Recorrer posiciones internas
    for i in range(1, filas-1):
        for j in range(1, columnas-1):

            # Árbol sano depende de los vecinos
            if matriz[i, j] == 1:

                # Revisar vecinos
                if (matriz[i-1, j] == 2 or matriz[i+1, j] == 2 or matriz[i, j-1] == 2 or matriz[i, j+1] == 2):
                    nueva[i, j] = 2

            # Árbol en fuego se convierte en ceniza
            elif matriz[i, j] == 2:
                nueva[i, j] = 3

    matriz = nueva  # Se intercambian las matrices

    # Se muestran los datos
    plt.imshow(matriz, cmap=colores, vmin=0, vmax=4)
    plt.title(f"Paso {paso}")
    plt.show()

    paso += 1   # Se incrementa el número de pasos