from collections import deque

# Main
if __name__ == "__main__":
    # Se pide la secuencia
    entrada = input("Secuencia de entrada: ").strip()

    cola_entrada = deque(map(int, entrada.split()))     # Se separa la entrada y con map se convierte cada elemento a int y luego a cola
    pila_auxiliar = []                                  # Pila vacía para invertir
    resultado = []                                      # Resultado final

    # Solicitar el valor de k
    try:
        k = int(input("Valor de k: "))
    except ValueError:
        print("Error: k debe ser un número entero positivo.")
        exit()

    # Validar condiciones de k
    if k <= 0 or k >= len(cola_entrada):
        print("Error: k debe ser mayor que 0 y menor que el tamaño de la secuencia.")
        exit()


    # 1. Extraer los primeros k elementos de la cola y pasarlos a la pila
    for n in range(k):
        elemento = cola_entrada.popleft()       # dequeue
        pila_auxiliar.append(elemento)          # push

    # 2. Invertir el orden de esos k elementos utilizando una pila
    while pila_auxiliar:
        elemento_invertido = pila_auxiliar.pop()  # pop
        resultado.append(elemento_invertido)

    # 3. Mantener el resto de los elementos en el mismo orden original
    while cola_entrada:
        elemento_restante = cola_entrada.popleft()
        resultado.append(elemento_restante)

    # Mostrar resultado final
    print("Resultado:", resultado)