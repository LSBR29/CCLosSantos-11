from collections import deque

# Función para invertir
def invertir(pila: deque):
    # Cadena vacía para el resultado
    resultado = ""

    # Mientras halla algo en la pila
    while len(pila) != 0:
        # Pop y se guarda en el resutado
        resultado += pila.pop()

    return resultado

def seleccionar(cadena: deque):
    # Pila vacía a invertir
    por_invertir = deque()

    # Se recorre la cadena como si fuese una cola
    while cadena:
        c = cadena.popleft()
        # Se añade cada caracter a la pila hasta llegar a encontrar "|"
        if c != "|":
            por_invertir.append(c)
        else:
            # Se detiene la selección
            break

    # Se retorna la pila a invertir
    return por_invertir

if __name__ == "__main__":
    # Se pide la cadena, se separa por letra y se convierte en cola
    cadena = deque(input("Ingrese cadena: "))
    resultado = ""

    while cadena:
        resultado += invertir(seleccionar(cadena))

    print(resultado)