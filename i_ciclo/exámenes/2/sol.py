import numpy as np
import matplotlib.pyplot as plt

# Crear el grafo no dirigido de amistades
# Cada persona es una clave, su valor es un conjunto de amigos
# Los nombres elegidos son: Ana (A), Carlos (B), Maria (C), Pedro (D), Luis (E)
red_social = {
    "Ana": {"Carlos", "Maria"},          # A -> B, C
    "Carlos": {"Ana", "Maria", "Luis"},  # B -> A, C, E
    "Maria": {"Ana", "Carlos", "Pedro"}, # C -> A, B, D
    "Pedro": {"Maria"},                  # D -> C
    "Luis": {"Carlos"}                   # E -> B
}

# Obtener lista de nombres en el orden de las claves del diccionario
personas = list(red_social.keys())

# Calcular el grado (número de amistades) de cada persona y guardarlo en una lista
grados = []
for persona in red_social:
    grados.append(len(red_social[persona]))

# Obtener el promedio de amigos
promedio = sum(grados) / len(grados)

# Crear un array de NumPy con los grados en el mismo orden que la lista de nombres
grados_array = np.array(grados)

# Imprimir resultados en consola
print("Nombres de las personas:", personas)
print("Promedio de amigos:", promedio)
print("Array de grados de amistad:", grados_array)

# Generar gráfico de barras
plt.bar(personas, grados_array, color="skyblue")

# Personalización del gráfico
plt.title("Número de amistades por persona")
plt.xlabel("Persona")
plt.ylabel("Cantidad de amistades")
plt.grid(axis='y', linestyle='--')   # Cuadrícula horizontal

# Mostrar el gráfico
plt.show()