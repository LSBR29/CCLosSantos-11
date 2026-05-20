import matplotlib.pyplot as plt

x = []
y = []

archivo = "C:\\Users\\santi\\Desktop\\CC\\Programación\\Github\\Undécimo\\i_ciclo\\ejercicios\\matplotlib\\soluciones\\test.txt"
with open(archivo, "r") as f:
    texto = f.readlines()

    for linea in texto:
        numeros = linea.split()

        x.append(int(numeros[0]))
        y.append(int(numeros[1]))

plt.plot(x, y)
plt.show()