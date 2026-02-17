# Función
def invertir(cadena: str):
    # Pila vacía
    pila = []

    # Cadena vacía para el resultado
    resultado = ""

    # Se recorre la cadena
    for c in cadena:
        # Push a cada caracter
        pila.append(c)

    # Mientras halla algo en la pila
    while len(pila) != 0:
        # Pop y se guarda en el resutado
        resultado += pila.pop()

    return resultado

# Main
if __name__ == "__main__":
    cadena = input("Ingrese la cadena a invertir: ")
    print(invertir(cadena))