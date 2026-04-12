class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def nuevoIzq(nodoActual, nuevoNodo):
    pass # Eliminar esta línea

def nuevoDer(nodoActual, nuevoNodo):
    pass # Eliminar esta línea

def construir(comandos):
    pass # Eliminar esta línea

def imprimirArbol(nodoActual, nivel=0):
    if nodoActual != None:
        imprimirArbol(nodoActual.der, nivel + 1)
        print(' ' * 4 * nivel + '-> ' + str(nodoActual.valor))
        imprimirArbol(nodoActual.izq, nivel + 1)

if __name__ == "__main__":
    comandos = [
        "ADD 10",
        "IZQ",
        "ADD 5",
        "IZQ",
        "ADD 3",
        "DER",
        "ADD 7",
        "DER",
        "ADD 15"
    ]

    raiz = construir(comandos)
    imprimirArbol(raiz)