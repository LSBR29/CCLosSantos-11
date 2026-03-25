class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar_extremo(nodo, nuevo, direccion):
    if direccion == "izquierda":
        if nodo.izq == None:
            nodo.izq = nuevo        # Inserta cuando encuentra espacio vacío
        else:
            insertar_extremo(nodo.izq, nuevo, direccion)  # Sigue bajando por la izquierda

    elif direccion == "derecha":
        if nodo.der == None:
            nodo.der = nuevo        # Inserta cuando encuentra espacio vacío
        else:
            insertar_extremo(nodo.der, nuevo, direccion)  # Sigue bajando por la derecha

def imprimirArbol(nodoActual, nivel=0):
    if nodoActual != None:
        imprimirArbol(nodoActual.der, nivel + 1)
        print(' ' * 4 * nivel + '-> ' + str(nodoActual.valor))
        imprimirArbol(nodoActual.izq, nivel + 1)

if __name__ == "__main__":
    raiz = Nodo(10)
    
    insertar_extremo(raiz, Nodo(5), "izquierda")
    insertar_extremo(raiz, Nodo(3), "izquierda")
    insertar_extremo(raiz, Nodo(20), "derecha")

    imprimirArbol(raiz)