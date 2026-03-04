# Se define la estructura básica
class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izq = None
        self.der = None

# Función recursiva para el total de nodos
def total_nodos(nodo: Nodo):
    if nodo == None:    # En cuanto se llega a un nodo vacío, se retorna 0
        return 0
    return 1 + total_nodos(nodo.izq) + total_nodos(nodo.der)    # Se retorna 1 más los nodos de los sub-árboles siguientes

# Función recursiva para el total de hojas
def total_hojas(nodo: Nodo):
    if nodo.izq == None and nodo.der == None:   # Si el nodo no tiene hijos se suma 1
        return 1
    return total_hojas(nodo.izq) + total_hojas(nodo.der)    # Se retorna el total de hojas en los sub-árboles siguientes

# Función recursiva para la altura
def altura(nodo: Nodo):
    if nodo == None:    # Si se está en el último nodo o el árbol está vacío, para empezar a contar en 0 se retorna -1
        return -1
    return 1 + max(altura(nodo.izq), altura(nodo.der))  # Se retorna 1 más la altura máxima encontrada en los sub-árboles

# Main
if __name__ == "__main__":
    # Creación del árbol
    raiz = Nodo(10)
    raiz.izq = Nodo(5)
    raiz.izq.izq = Nodo(3)
    raiz.izq.der = Nodo(7)
    raiz.der = Nodo(15)

    # Impresión de los datos
    print(f"Total de nodos: {total_nodos(raiz)}")
    print(f"Total de hojas: {total_hojas(raiz)}")
    print(f"Altura: {altura(raiz)}")