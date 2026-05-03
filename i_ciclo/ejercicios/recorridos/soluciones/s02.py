def encontrar(grafo, nodo, destino, visitados=None, rutas=None):
    if visitados is None:       # Al inicio se crea la lista de visitados vacía
        visitados = []

    if rutas is None:           # Al inicio se crea una lista de rutas vacía
        rutas = []

    visitados.append(nodo)      # Marcar el nodo actual como visitado

    if nodo == destino:     # Caso base, si se llega al destino se guarda la ruta
        rutas.append(visitados.copy())
    else:
        for vecino in grafo[nodo]:       # Recorre cada vecino conectado al nodo actual
            if vecino not in visitados:     # Solo visita el vecino si no ha sido procesado antes
                encontrar(grafo, vecino, destino, visitados, rutas)

    visitados.pop()     # Se elimina el nodo de la lista de visitados para permitir revisitarlo

    return rutas

if __name__ == "__main__":
    """
    A -- B -- C
    |    |
    D ----
    """
    grafo = {
        'A': {'B', 'D'},
        'B': {'A', 'C', 'D'},
        'C': {'B'},
        'D': {'A', 'B'}
    }

    inicial = "A"
    destino = "C"

    print(f"Ciudad inicial: {inicial}")
    print(f"Ciudad destino: {destino}")
    print(f"Rutas posibles: {encontrar(grafo, inicial, destino)}")