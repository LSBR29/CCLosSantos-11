# Se define la estructura básica
class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izq = None
        self.der = None

# Función recursiva para ver si hay un camino cuya suma es igual al objetivo
# La idea es ir restando el valor del nodo al objetivo hasta llegar a 0, si no es posible, el camino no existe
def existe_camino_suma(nodo: Nodo, objetivo: int):
    if nodo == None:
        return False

    # Si es hoja, verificamos si la suma coincide
    if nodo.izq == None and nodo.der == None:
        return nodo.valor == objetivo
    
    # Restamos el valor actual al objetivo
    nuevo_objetivo = objetivo - nodo.valor
    
    # Se revisan los subárboles, si algún camino dió True la salida es True
    return existe_camino_suma(nodo.izq, nuevo_objetivo) or existe_camino_suma(nodo.der, nuevo_objetivo)

# Main
if __name__ == "__main__":
    # Creación del árbol
    raiz = Nodo(5)
    raiz.izq = Nodo(4)
    raiz.der = Nodo(8)

    raiz.izq.izq = Nodo(11)
    raiz.izq.izq.izq = Nodo(7)
    raiz.izq.izq.der = Nodo(2)

    raiz.der.izq = Nodo(13)
    raiz.der.der = Nodo(4)

    print("Objetivo 22:", existe_camino_suma(raiz, 22))
    print("Objetivo 26:", existe_camino_suma(raiz, 26))
    print("Objetivo 19:", existe_camino_suma(raiz, 19))