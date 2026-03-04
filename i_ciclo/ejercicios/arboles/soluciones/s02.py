# Se define la estructura básica
class Nodo:
    def __init__(self, valor: int):
        self.valor = valor
        self.izq = None
        self.der = None

# Función para buscar de forma recursiva
def buscar(nodo: Nodo, valor):
    if nodo == None:    # Si el nodo está vació se devuelve False y se continua recorriendo
        return False
    
    if nodo.valor == valor:     # Si se halla el valor esperado se devuelve True y se continua recorriendo
        return True
    
    return buscar(nodo.izq, valor) or buscar(nodo.der, valor)   # OR retorna True si una de las respuestas fue True

# Main
if __name__ == "__main__":
    # Creación del árbol
    raiz = Nodo(10)
    raiz.izq = Nodo(5)
    raiz.izq.izq = Nodo(3)
    raiz.izq.der = Nodo(7)
    raiz.der = Nodo(15)

    # Dato a buscar
    n = 9

    # Impresión de los datos
    print(f"Buscar {n}: {buscar(raiz, n)}")
