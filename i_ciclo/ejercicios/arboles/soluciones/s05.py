from s03 import son_iguales

# Se define la estructura básica
class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izq = None
        self.der = None

def es_subarbol(A, B):
    # Árbol vacío siempre es sub-árbol
    if B == None:
        return True
    
    # Si se llega a un árbol o sub-árbol vacío no son iguales
    if A == None:
        return False
    
    # Se revisa si son iguales el árbol o sub-árbol actual al que se está buscando
    if son_iguales(A, B):
        return True
    
    # Se revisan los sub-árboles, si alguno dió True la salida es True
    return es_subarbol(A.izq, B) or es_subarbol(A.der, B)

# Main
if __name__ == "__main__":
    # Árbol A
    A = Nodo(3)
    A.izq = Nodo(4)
    A.der = Nodo(5)
    A.izq.izq = Nodo(1)
    A.izq.der = Nodo(2)

    # Árbol B
    B = Nodo(4)
    B.izq = Nodo(1)
    B.der = Nodo(2)

    # Árbol C
    C = Nodo(4)
    C.izq = Nodo(1)
    C.der = Nodo(3)

    print(f"B subárbol de A: {es_subarbol(A, B)}")
    print(f"C subárbol de A: {es_subarbol(A, C)}")