"""
1. a
2. b
3. a
4. a
5. b
6. c
7. c
8. a
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def nuevoIzq(nodoActual, nuevoNodo):
    if nodoActual.izq == None:
        nodoActual.izq = nuevoNodo
    else:
        nuevoIzq(nodoActual.izq, nuevoNodo)

def nuevoDer(nodoActual, nuevoNodo):
    if nodoActual.der == None:
        nodoActual.der = nuevoNodo
    else:
        nuevoDer(nodoActual.der, nuevoNodo)

def construir(comandos):
    posActual = None
    arbol = []

    while comandos:
        ejecutando = comandos.pop(0).split()
        
        if ejecutando[0] == "ADD":
            nodoNuevo = Nodo(int(ejecutando[1]))

            if posActual == "IZQ":
                nuevoIzq(arbol[0], nodoNuevo)
            elif posActual == "DER":
                nuevoDer(arbol[0], nodoNuevo)

            arbol.append(nodoNuevo)
            imprimirArbol(arbol[0])

        elif ejecutando[0] == "IZQ":
            posActual = "IZQ"

        elif ejecutando[0] == "DER":
            posActual = "DER"

    return arbol[0]

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