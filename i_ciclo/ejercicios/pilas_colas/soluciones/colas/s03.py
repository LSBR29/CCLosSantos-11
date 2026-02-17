from collections import deque

# Función
def maximos(lista: list, k: int):
    # Cola vacía y lista para máximos
    cola = deque()
    maximos = []

    # Se revisan los números en la lista y se encolan
    for n in lista:
        cola.append(n)

        # Cuándo la cola sea del tamaño necesario se busca el máximo y se guarda
        if len(cola) == k:
            maximos.append(max(cola))

            # Se desencola para reducir el tamaño en 1 y provocar que se añada el siguiente elemento
            cola.popleft()

    # Se retornan los máximos
    return maximos

# Main
if __name__ == "__main__":
    # Cola y k definidos
    numeros = [2, 1, 3, 4, 6, 3, 8, 9, 10, 12, 56]
    k = 4

    print(f"Lista: {numeros}")
    print(f"k: {k}")

    # Se imprime el resultado con espacios en blanco
    resultado = maximos(numeros, k)
    for n in resultado:
        print(n, end=" ")