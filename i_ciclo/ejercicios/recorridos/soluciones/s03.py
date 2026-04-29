def hay_camino(matriz, x_ini, y_ini, x_fin, y_fin):     # BFS
    visitados = []      # Lista de posiciones ya visitadas para no repetir

    cola = [(x_ini, y_ini)]     # Cola de BFS con posiciones (x, y)

    # Dimensiones de la matriz
    filas = len(matriz)
    columnas = len(matriz[0])

    while cola:
        x, y = cola.pop(0) # Se extrae la primera posición

        # VALIDACIONES
        if x < 0 or y < 0 or x >= filas or y >= columnas:
            continue    # Si está fuera de la matriz, se ignora

        if matriz[x][y] == 1:
            continue    # Si es una pared (1), no se puede pasar

        if (x, y) in visitados:
            continue    # Si ya fue visitado, se ignora para evitar ciclos

        visitados.append((x, y))

        # Si se llegó al final, hay camino
        if x == x_fin and y == y_fin:
            return True

        # Nuevos caminos a revisar
        cola.append((x, y-1))   # abajo
        cola.append((x, y+1))   # arriba
        cola.append((x+1, y))   # derecha
        cola.append((x-1, y))   # izquierda

    return False    # Si se vacía la cola y no se llegó al destino, no existe camino

if __name__ == "__main__":
    matriz = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 0, 0]
    ]

    print("Existe camino:", hay_camino(matriz, 0, 0, 2, 2))