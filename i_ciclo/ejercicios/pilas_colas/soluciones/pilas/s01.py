# Función
def verificar_parentesis(cadena: str):
    # Pila vacía
    pila = []

    # Se recorre la cadena
    for p in cadena:

        # Si se encuentra (, push
        if p == "(":
            pila.append(p)

        # Si se encuentra ), pop
        else:
            # Pero si está vacía, error, o sea no está balanceada
            if len(pila) == 0:
                return False
            else:
                pila.pop()

    # Si al final la pila está vacía por cada ) encontrado se eliminó un (, 
    # o sea la cadena está balanceada.
    if len(pila) == 0:
        return True

    # Si no, retorna False
    return False

# Main
if __name__ == "__main__":
    cadena = input("Ingrese la cadena a verificar: ")
    print(verificar_parentesis(cadena))