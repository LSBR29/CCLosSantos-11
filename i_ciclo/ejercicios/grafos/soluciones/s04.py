def masCara(grafo):
    conexionCara = ""       # Guarda la conexión con mayor costo encontrada
    costoMax = 0        # Guarda el costo máximo encontrado

    for nodo in grafo:      # Recorre cada nodo del grafo
        # Recorre cada conexión del nodo actual
        # Cada conexión es una tupla: (vecino, peso)
        for conexion in grafo[nodo]:
            if conexion[1] > costoMax:      # Si el peso de la conexión actual es mayor al máximo registrado
                costoMax = conexion[1]      # Actualiza el costo máximo
                conexionCara = f"{nodo} - {conexion[0]}"    # Guarda la conexión en formato "nodo - vecino"

    return (conexionCara, costoMax)

if __name__ == "__main__":
    """
      A --(500)-- B
      |           |
    (300)       (800)
      |           |
      C --(200)-- D
    """
    grafo = {
        'A': {('B', 500), ('C', 300)},
        'B': {('A', 500), ('D', 800)},
        'C': {('A', 300), ('D', 200)},
        'D': {('B', 800), ('C', 200)},
    }

    print(f"Conexión más cara: {masCara(grafo)[0]}")
    print(f"Costo: {masCara(grafo)[1]}")