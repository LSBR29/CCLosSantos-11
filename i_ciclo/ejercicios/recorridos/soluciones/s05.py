def propagacion(grafo, nodo):   # BFS
    visitados = []
    cola = [nodo]
    orden = []      # Guarda el orden en que se enteran de la noticia

    while cola:
        nodo = cola.pop(0)

        if nodo not in visitados:
            visitados.append(nodo)      # Visitado = Enterado

            orden.append(nodo)      # Se agrega al orden de propagación

            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

    return orden

if __name__ == "__main__":
    grafo = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B'},
        'D': {'B'}
    }

    print("Orden de propagación:", propagacion(grafo, 'A'))