# Main
if __name__  == "__main__":
    # Pila vacía
    pila = []

    while True:
        # Comando a usar
        comando = input("> ")

        # Si el comando empieza con escribir
        if comando.startswith("escribir "):
            # Se toma el texto a partir del índice 9, o sea, se ignora "escribir " y se hace push a la pila
            palabra = comando[9:]
            pila.append(palabra)

        # Si el comando es undo, se hace pop
        elif comando == "undo":
            if pila:
                pila.pop()

        # Si el comando es salir se rompe el ciclo
        elif comando == "salir":
            break

    # Se pegan las palabras que quedaron en la pila y se imprimen
    texto_final = " ".join(pila)
    print(texto_final)