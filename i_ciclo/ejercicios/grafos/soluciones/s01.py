def estan_conectados(grafo, nodo1, nodo2):
    # Verificar si nodo1 existe en el grafo
    if nodo1 not in grafo:
        return False
    
    # Revisa si nodo2 está en la lista de adyacencia de nodo1
    return nodo2 in grafo[nodo1]

    """OTRA FORMA
    if nodo2 in grafo[nodo1]:
        return True
    else:
        return False
    """

if __name__ == "__main__":
    grafo = {
        'A': {'B', 'C'},
        'B': {'A', 'D'},
        'C': {'A'},
        'D': {'B'}
    }

    print("A - B:", estan_conectados(grafo, 'A', 'B'))
    print("A - D:", estan_conectados(grafo, 'A', 'D'))