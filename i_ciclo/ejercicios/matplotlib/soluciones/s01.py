import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [2, 4, 6, 8, 10, 12, 14, 16]
y2 = [1, 4, 9, 16, 25, 36, 49, 64]

# '-' hace que sea una línea continua, 'o' pone círculos como marcadores y 'r' convierte a color rojo
plt.plot(x, y1, "-or")

# '--' hace que sea una línea discontinua, '*' pone estrellas como marcadores y 'm' convierte a color magenta
plt.plot(x, y2, "--*m")

plt.legend(["*2", "^2"])    # Para colocar una leyenda
plt.title("Gráfico con varias líneas")
plt.xlabel("Números")
plt.ylabel("Resultados")
plt.show()  # Mostrar gráficos