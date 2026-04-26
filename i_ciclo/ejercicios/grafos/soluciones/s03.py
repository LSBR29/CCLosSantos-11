def personas_infectadas(grafo, inicio):
    infectados = []             # Lista de infectados
    recorrido = [inicio]        # Se hará una simulación de comoo se propagó la infección

    while recorrido:
        nodo = recorrido.pop(0) # Se maneja el recorrido como una cola
                                # Es como repetir la propagación de la infección

        if nodo in infectados:  # Si ya lo contamos como infectado continuamos
            continue

        infectados.append(nodo) # Si no, al estar en el recorrido es porque está infectado

        for vecino in grafo[nodo]:  # Revisamos sus vecinos para agregarlos al recorrido si no los hemos tomado en cuenta
            if vecino not in infectados:
                recorrido.append(vecino)

    return len(infectados)

if __name__ == "__main__":
    grafo = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B'},
        'D': {'B'},
        'E': {'F'},
        'F': {'E'}
    }

    cantidad = personas_infectadas(grafo, 'A')

    print("Personas infectadas:", cantidad)