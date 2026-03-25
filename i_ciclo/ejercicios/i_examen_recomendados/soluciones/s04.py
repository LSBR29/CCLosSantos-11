class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def profundidad(nodo, valor, nivel=0):
    if nodo == None:
        return -1               # Caso base: no se encontró el valor
    
    if nodo.valor == valor:
        return nivel            # Retorna el nivel donde se encontró el valor
    else:
        # Busca en ambos lados y toma el mayor resultado
        return max(
            profundidad(nodo.izq, valor, nivel + 1),
            profundidad(nodo.der, valor, nivel + 1)
        )

def imprimirArbol(nodoActual, nivel=0):
    if nodoActual != None:
        imprimirArbol(nodoActual.der, nivel + 1)
        print(' ' * 4 * nivel + '-> ' + str(nodoActual.valor))
        imprimirArbol(nodoActual.izq, nivel + 1)

if __name__ == "__main__":
    raiz = Nodo(10)

    raiz.izq = Nodo(5)
    raiz.der = Nodo(15)

    raiz.izq.izq = Nodo(3)
    raiz.izq.der = Nodo(7)

    print("Arbol: ")
    imprimirArbol(raiz)
    print("")
    
    print(f"Profundidad de 10: {profundidad(raiz, 10)}")
    print(f"Profundidad de 7: {profundidad(raiz, 7)}")
    print(f"Profundidad de 15: {profundidad(raiz, 15)}")
    print(f"Profundidad de 8: {profundidad(raiz, 8)}")