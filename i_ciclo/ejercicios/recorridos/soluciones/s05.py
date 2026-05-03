def propagacion(grafo, nodo):       # BFS
    visitados = []      # Al inicio se crea la lista de visitados vacía
    cola = [nodo]       # Una cola para ir avanzando
    orden = []

    while cola:     # Repetir hasta que se revisen todos los nodos
        nodo = cola.pop(0)      # Se extrae el nodo a revisar de la cola
        visitados.append(nodo)      # Se guarda como visitado

        orden.append(nodo)     # Operación sobre el nodo

        for vecino in grafo[nodo]:       # Recorre cada vecino conectado al nodo actual
            if vecino not in visitados:     # Solo encolan vecinos que no hayan sido visitados aún
                cola.append(vecino)
        
    return orden

if __name__ == "__main__":
    """
    A -- B -- C
         |
         D
    """
    grafo = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B'},
        'D': {'B'}
    }

    print("Orden de propagación:", propagacion(grafo, 'A'))