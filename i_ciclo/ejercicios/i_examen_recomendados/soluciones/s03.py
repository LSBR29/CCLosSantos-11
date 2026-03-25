def operar(instrucciones):
    pila = []
    modo = None            # Guarda el modo actual

    while instrucciones:
        actual = instrucciones.pop(0)  # Toma el priemr elemento (cola)

        if actual == "MODO_A":
            modo = "A"                # Modo agregar
        elif actual == "MODO_E":
            modo = "E"                # Modo eliminar
        else:
            if modo == "A":
                pila.append(1)        # Agrega un 1 a la pila
            elif modo == "E":
                pila.pop()            # Elimina el último elemento de la pila

            print(pila)               # Imprime la pila

if __name__ == "__main__":
    instrucciones = ["MODO_A", "ACCION", "ACCION", "MODO_E", "ACCION", "MODO_A", "ACCION"]

    operar(instrucciones)