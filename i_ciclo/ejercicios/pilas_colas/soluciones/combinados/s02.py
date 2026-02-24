# Main
if __name__  == "__main__":
    # Pila vacía
    pila = []

    # Se piden los comandos infinitamente y se ejecutan uno a uno como si fuese una cola
    while True:
        # Comando a usar
        comando = input()

        # Si está vacio terminar el ciclo para salir
        if comando == "":
            break

        # Separar el comando como lista para ver si es NUM, MUL o SUM
        partes = comando.split()

        # Si empieza por NUM se toma el siguiente elemento y se añade como int a la pila
        if partes[0] == "NUM":
            pila.append(int(partes[1]))

        # Si empieza por SUM se revisa que se pueda hacer la suma de los últimos 2 añadidos y se hace
        elif partes[0] == "SUM":
            if len(pila) < 2:
                print("No hay suficientes números para SUM")
                continue
            a = pila.pop()
            b = pila.pop()
            pila.append(a + b)

        # Si empieza por MUL se revisa que se pueda hacer la multiplicación de los últimos 2 añadidos y se hace
        elif partes[0] == "MUL":
            if len(pila) < 2:
                print("No hay suficientes números para MUL")
                continue
            a = pila.pop()
            b = pila.pop()
            pila.append(a * b)

        else:
            print("Comando no reconocido")

    # Se imprime lo último añadido a la pila
    print("RESULTADO:", pila[-1])