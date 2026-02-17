from collections import deque

# Función
def rotar(cola: deque, k: int):
    # Se desencolan y encolan los primeros k elementos
    while k != 0:
        cola.append(cola.popleft())

        # Se resta a k para ir avanzando hasta alcanzar la cantidad de rotaciones necesarias
        k -= 1

    # Se retorna la cola rotada
    return cola

# Main
if __name__ == "__main__":
    # Cola y k definidos
    numeros = deque([1, 2, 3, 4, 5])
    k = 2

    print(f"Lista: {numeros}")
    print(f"k: {k}")

    # Se imprime el resultado con espacios en blanco
    resultado = rotar(numeros, k)
    for n in resultado:
        print(n, end=" ")