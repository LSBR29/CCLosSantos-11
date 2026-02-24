from collections import deque

# Main
if __name__ == "__main__":
    # Se pide la secuencia
    entrada = input("Secuencia de entrada: ").strip()

    cola_entrada = deque(map(int, entrada.split()))     # Se separa la entrada y con map se convierte cada elemento a int y luego a cola
    pila_auxiliar = []                                  # Pila vacía
    cola_salida = deque()                               # Cola vacía

    tamano = len(cola_entrada)             # Tamaño de la secuencia para verificar al final
    esperado = 1                           # Número esperado en la secuencia

    # Mientras haya elementos en la cola de entrada, se toma el siguiente posible y se revisa si es el esperado
    while cola_entrada:
        siguiente = cola_entrada.popleft()

        # Si es el esperado, se añade a la salida y el esperado aumenta en 1
        if siguiente == esperado:
            cola_salida.append(siguiente)
            esperado += 1

        # Si no es el esperado, se añade a la auxiliar
        else:
            pila_auxiliar.append(siguiente)

    # Depués de revisar la entrada, se revisa la auxiliar
    while pila_auxiliar:
        siguiente = pila_auxiliar.pop()

        # Si el siguiente posible en la auxiliar es el esperado, se añade a la salida y el esperado aumenta en 1
        if siguiente == esperado:
            cola_salida.append(siguiente)
            esperado += 1

        # Si no es el esperado, como ya se revisó la entrada, significa que no se puede seguir, y se rompe el ciclo        
        else:
            break

    # Si al final la salida tiene el tamaño de la secuencia original, si se pudo ordenar
    if len(cola_salida) == tamano:
        print(f"Sí es posible ordenarla en {list(cola_salida)}")

    # Si no, significa que quedó algún número en la entrada o la auxiliar y no se pudo ordenar
    else:
        print("No es posible ordenarla")