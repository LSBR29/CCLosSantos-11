def recomendar_amigos(grafo, usuario):
    recomendaciones = []
    amigos = grafo[usuario] # Amigos del usuario

    # Revisar amigos del usuario
    for amigo in amigos:
        for posible in grafo[amigo]: # Revisar los amigos del amigo del usuario (posible)
            # Condiciones:
            # - No ser el mismo usuario
            # - No ser amigo actual
            # - No estar ya recomendado
            if (posible != usuario and
                posible not in amigos and
                posible not in recomendaciones):
                
                recomendaciones.append(posible)

    return recomendaciones

if __name__ == "__main__":
    grafo = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['B'],
        'D': ['B']
    }

    recs = recomendar_amigos(grafo, 'A')

    print("Recomendaciones:", recs)