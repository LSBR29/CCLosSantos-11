def procesar(instrucciones):
    resultado = 0
    operacion = None       # Guarda la operación a realizar

    while instrucciones:
        actual = instrucciones.pop(0)  # Toma el primer elemento (cola)

        if actual == "SUMA":
            operacion = "S"            # Cambia el tipo de operación a suma
        elif actual == "MULT":
            operacion = "M"            # Cambia el tipo de operación a multiplicación
        else:                          # Si no es suma ni resta es un número
            num = int(actual)
            if operacion == "S":
                resultado += num       # Aplica suma
            elif operacion == "M":
                resultado *= num       # Aplica multiplicación

    return resultado

if __name__ == "__main__":
    instrucciones = ["SUMA", "5", "MULT", "3", "SUMA", "2"]

    print(procesar(instrucciones))