def encontrarCondicionado(grafo, nodo, destino, k, visitados=None, rutas=None):
    if visitados is None:       # Al inicio se crea la lista de visitados vacía
        visitados = []

    if rutas is None:           # Al inicio se crea una lista de rutas vacía
        rutas = []

    visitados.append(nodo)      # Marcar el nodo actual como visitado

    if nodo == destino and len(visitados) == k:     # Caso base, si se llega al destino y la ruta tiene el tamaño esperado
        rutas.append(visitados.copy())              # se guarda
    else:
        for vecino in grafo[nodo]:       # Recorre cada vecino conectado al nodo actual
            if vecino not in visitados:     # Solo visita el vecino si no ha sido procesado antes
                encontrarCondicionado(grafo, vecino, destino, k, visitados, rutas)

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
    k = 3

    print(f"Inicio: {inicial}")
    print(f"Fin: {destino}")
    print(f"k: {k}")
    print(f"Caminos válidos: {encontrarCondicionado(grafo, inicial, destino, k)}")