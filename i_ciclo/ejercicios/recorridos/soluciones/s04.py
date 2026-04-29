def dfs(matriz, filas, columnas, x, y):
    # Si está fuera de la matriz o es agua (0), se detiene
    if x < 0 or x >= filas or y < 0 or y >= columnas or matriz[x][y] == 0:
        return

    matriz[x][y] = 0   # Se marca como visitado "borrando" la tierra

    # Se visitan las 4 direcciones posibles
    dfs(matriz, filas, columnas, x, y-1)   # abajo
    dfs(matriz, filas, columnas, x, y+1)   # arriba
    dfs(matriz, filas, columnas, x+1, y)   # derecha
    dfs(matriz, filas, columnas, x-1, y)   # izquierda


def numero_islas(matriz):
    contador = 0    # Cuenta cuántas islas se encuentran

    # Dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    for x in range(filas):
        for y in range(columnas):

            if matriz[x][y] == 1:       # Si encontramos tierra (1), es una nueva isla
                dfs(matriz, filas, columnas, x, y)      # Se recorre y "elimina" toda la isla
                contador += 1   # Se incrementa el número de islas

    return contador

if __name__ == "__main__":
    matriz = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0]
    ]

    print("Número de islas:", numero_islas(matriz))