def alcanzables(grafo, nodo, visitados=None):
    if visitados is None:       # Al inicio se crea la lista de visitados vacía
        visitados = []

    visitados.append(nodo)      # Marcar el nodo actual como visitado

    for vecino in grafo[nodo]:       # Recorre cada vecino conectado al nodo actual
        if vecino not in visitados:     # Solo visita el vecino si no ha sido procesado antes
            alcanzables(grafo, vecino, visitados)

    return visitados

if __name__ == "__main__":
    """
    A -- B      C -- D
                |
                E
    """
    grafo = {
        'A': {'B'},
        'B': {'A'},
        'C': {'D', 'E'},
        'D': {'C'},
        'E': {'C'}
    }

    inicial = "A"
    print(f"Computadora inicial: {inicial}")
    print(f"Computadoras alcanzables: {alcanzables(grafo, inicial)}")