# Se define la estructura básica
class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izq = None
        self.der = None

# Función para comparar dos árboles
def son_iguales(nodo1: Nodo, nodo2: Nodo):
    if nodo1 == None and nodo2 == None:    # Ambos son vacíos
        return True
    
    if nodo1 == None or nodo2 == None:    # Uno es vacío y el otro no
        return False
    
    # En otro caso se tiene que cumplir que los valores sean iguales y que los sub-árboles sean iguales
    return nodo1.valor == nodo2.valor and son_iguales(nodo1.izq, nodo2.izq) and son_iguales(nodo1.der, nodo2.der)

# Main
if __name__ == "__main__":
    # Árbol A
    A = Nodo(4)
    A.izq = Nodo(2)
    A.der = Nodo(6)

    # Árbol B
    B = Nodo(4)
    B.izq = Nodo(2)
    B.der = Nodo(6)

    # Árbol C
    C = Nodo(4)
    C.izq = Nodo(2)
    C.der = Nodo(7)

    print(f"Iguales A y B: {son_iguales(A, B)}")
    print(f"Iguales A y C: {son_iguales(A, C)}")