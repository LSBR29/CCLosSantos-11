def conexiones(grafo, nodo):
    visitados = []      # Al inicio se crea la lista de visitados vacía
    cola = [nodo]       # Una cola para ir avanzando
    distancias = {nodo: 0}

    while cola:     # Repetir hasta que se revisen todos los nodos
        nodo = cola.pop(0)      # Se extrae el nodo a revisar de la cola
        visitados.append(nodo)      # Se guarda como visitado
        
        for vecino in grafo[nodo]:       # Recorre cada vecino conectado al nodo actual
            if vecino not in visitados:     # Solo encolan vecinos que no hayan sido visitados aún
                cola.append(vecino)
                distancias[vecino] = distancias[nodo] + 1       # La distancia de un vecino es la distancia del anterior + 1

    return distancias

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

    inicial = "A"

    print(f"Personas inicial: {inicial}")
    print(f"Distancias: {conexiones(grafo, inicial)}")