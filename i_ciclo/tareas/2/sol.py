import numpy as np
import matplotlib.pyplot as plt
import math

# Cantidades de puntos
valores_n = [10, 100, 1000, 10000, 100000]

# Lista para guardar las aproximaciones
aproximaciones = []

# Repetir para cada cantidad de puntos
for n in valores_n:
    # Generar puntos aleatorios entre 0 y 1
    x = np.random.rand(n)
    y = np.random.rand(n)

    # Verificar cuáles puntos están dentro del cuarto de círculo
    dentro = (x**2 + y**2) <= 1

    # Contar puntos dentro
    cantidad_dentro = dentro[dentro == True].size

    # Calcular aproximación de pi
    pi_aproximado = 4 * (cantidad_dentro / n)

    # Calcular error
    error = abs(math.pi - pi_aproximado) / (math.pi) * 100

    # Guardar resultado
    aproximaciones.append(pi_aproximado)
    
    # Mostrar resultado
    print(f"N = {n:<8}: {pi_aproximado:.6f} | Error: {error:.2f}%")

# Graficar aproximaciones
plt.plot(valores_n, aproximaciones)

# Título y etiquetas
plt.title("Estimación de pi")
plt.xlabel("Cantidad de puntos")
plt.ylabel("Valor")

# Escala logarítmica
plt.xscale("log")

# Mostrar malla
plt.grid()

# Mostrar gráfica
plt.show()