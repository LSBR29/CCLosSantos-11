def tiempo_propagacion(grafo, inicio):      # BFS
    visitados = []      # Lista para no repetir nodos (personas ya infectadas)

    cola = [(inicio, 0)]        # Guarda (nodo, tiempo)
    tiempo_max = 0      # Resultado

    while cola:
        nodo, tiempo = cola.pop(0)

        if nodo not in visitados:
            visitados.append(nodo)      # Ya visitado = infectado
            tiempo_max = max(tiempo_max, tiempo)        # Se actualiza el tiempo

            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append((vecino, tiempo + 1))

    return tiempo_max

if __name__ == "__main__":
    grafo = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B'},
        'D': {'B'}
    }

    print(f"Tiempo total de propagación: {tiempo_propagacion(grafo, 'A')} minutos")