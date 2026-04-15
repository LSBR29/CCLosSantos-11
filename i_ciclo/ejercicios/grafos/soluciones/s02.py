def nodo_mas_conectado(grafo):
    max_nodo = None
    max_grado = 0

    for nodo in grafo:            # Revisar cada nodo
        grado = len(grafo[nodo])  # Cantidad de vecinos

        if grado > max_grado:     # Intercambiar si hay uno con más vecinos
            max_grado = grado
            max_nodo = nodo

    return max_nodo, max_grado    # Retornar ambas variables

if __name__ == "__main__":
    grafo = {
        'A': {'B', 'D'},
        'B': {'A', 'C', 'E'},
        'C': {'B'},
        'D': {'A'},
        'E': {'B'}
    }

    nodo, conexiones = nodo_mas_conectado(grafo)

    print("Nodo más conectado:", nodo)
    print("Cantidad de conexiones:", conexiones)