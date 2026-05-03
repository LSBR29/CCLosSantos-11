def dfs(grafo, nodo, visitados=None):
    visitados.append(nodo)      # Marcar el nodo actual como visitado

    for vecino in grafo[nodo]:       # Recorre cada vecino conectado al nodo actual
        if vecino not in visitados:     # Solo visita el vecino si no ha sido procesado antes
            dfs(grafo, vecino, visitados)

def islas(grafo):
    visitados = []      # Lista de visitados vacía
    grupos = 0          # Grupos en 0 al inicio

    for nodo in grafo:      # Se va a hacer dfs apartir de todos lo nodos que no se hayan visitado
        if nodo not in visitados:
            dfs(grafo, nodo, visitados)
            grupos += 1     # Cada búsqueda que se hace significa un grupo nuevo

    return grupos

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

    print(f"Numero de grupos: {islas(grafo)}")