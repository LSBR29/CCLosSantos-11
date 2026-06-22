import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el grafo no dirigido con 6 ciudades
# Cada ciudad es una clave, su valor es un conjunto de ciudades conectadas directamente
grafo = {
    "San José": {"Alajuela", "Cartago"},
    "Alajuela": {"San José", "Heredia", "Puntarenas"},
    "Cartago": {"San José"},
    "Heredia": {"Alajuela", "Limon"},
    "Puntarenas": {"Alajuela"},
    "Limon": {"Heredia"}
}

# 2. Calcular grado (número de conexiones) de cada ciudad
grados = {}          # diccionario para guardar ciudad:grado
for ciudad in grafo:
    grados[ciudad] = len(grafo[ciudad])   # cantidad de vecinos

# 3. Encontrar la ciudad con más conexiones
max_ciudad = None
max_grado = 0
for ciudad, grado in grados.items():
    if grado > max_grado:
        max_grado = grado
        max_ciudad = ciudad

# 4. Calcular el promedio de conexiones
total_conexiones = sum(list(grados.values()))
cantidad_ciudades = len(grados)
promedio = total_conexiones / cantidad_ciudades

# 5. Crear un array de NumPy con los grados en el orden de las claves
# Para mantener consistencia con el gráfico, usamos el mismo orden de las claves
ciudades = list(grados.keys())          # lista de nombres en orden
grados_array = np.array(list(grados.values()))   # array de NumPy

# 6. Imprimir resultados
print("Array de NumPy con los grados:", grados_array)
print(f"Ciudad más conectada: {max_ciudad} con {max_grado} conexiones")
print(f"Promedio de conexiones: {promedio:.2f}")

# 7. Generar gráfico de barras
plt.bar(ciudades, grados_array)

# Personalización del gráfico
plt.title("Conexiones por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Número de conexiones")
plt.grid(axis='y', linestyle='--')   # Cuadrícula horizontal

# Mostrar el gráfico
plt.show()