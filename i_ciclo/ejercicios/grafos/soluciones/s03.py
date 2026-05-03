def recomendar_amigos(grafo, usuario):
    recomendaciones = set()
    amigos = grafo[usuario] # Amigos del usuario

    # Revisar amigos del usuario
    for amigo in amigos:
        posibles = grafo[amigo]

        for posible in posibles: # Revisar los amigos del amigo del usuario
            # Condiciones:
            # - No ser el mismo usuario
            # - No ser amigo actual
            # - No estar ya recomendado
            if (posible != usuario and posible not in amigos):
                recomendaciones.add(posible)

    return (amigos, recomendaciones)

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

    usuario = "A"
    recs = recomendar_amigos(grafo, usuario)

    print(f"Usuario: {usuario}")
    print(f"Amigos Actuales: {recs[0]}")
    print(f"Recomendaciones: {recs[1]}")