def contar_caminos(grafo, actual, destino, visitados):      # DFS
    if actual == destino:           # Caso base: al llegar al destino es un camino encontrado
        return 1

    visitados.append(actual)
    caminos = 0     # Contador de caminos desde este nodo hacia el destino

    for vecino in grafo[actual]:
        if vecino not in visitados:
            caminos += contar_caminos(grafo, vecino, destino, visitados)    # Sumamos los caminos encontrados desde ese vecino

    visitados.pop()     # Se quita el nodo actual para permitir que se use en otros caminos diferentes

    return caminos

if __name__ == "__main__":
    grafo = {
        'A': {'B', 'C'},
        'B': {'A', 'C', 'D'},
        'C': {'A', 'B'},
        'D': {'B'}
    }

    print("Cantidad de caminos:", contar_caminos(grafo, 'A', 'D', []))