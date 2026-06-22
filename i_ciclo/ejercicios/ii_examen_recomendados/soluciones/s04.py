import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el grafo ponderado no dirigido con 6 planetas
# Cada planeta tiene un conjunto de tuplas (vecino, distancia)
sistema_solar = {
    "Mercurio": {("Venus", 50), ("Tierra", 90)},
    "Venus": {("Mercurio", 50), ("Tierra", 40), ("Marte", 120)},
    "Tierra": {("Mercurio", 90), ("Venus", 40), ("Marte", 70), ("Júpiter", 150)},
    "Marte": {("Venus", 120), ("Tierra", 70), ("Júpiter", 100), ("Saturno", 180)},
    "Júpiter": {("Tierra", 150), ("Marte", 100), ("Saturno", 60)},
    "Saturno": {("Marte", 180), ("Júpiter", 60)}
}

# 2. Calcular grado (número de rutas) de cada planeta
grados = {}
for planeta in sistema_solar:
    grados[planeta] = len(sistema_solar[planeta])   # cada tupla es una ruta

# 3. Calcular distancia total acumulada de cada planeta (suma de pesos de sus rutas)
distancias_totales = {}
for planeta in sistema_solar:
    total = 0
    for vecino, distancia in sistema_solar[planeta]:   # cada ruta es tupla (vecino, distancia)
        total += distancia
    distancias_totales[planeta] = total

# 4. Encontrar el planeta con más rutas (más conectado)
max_grado = 0
planeta_mas_conectado = None
for planeta, grado in grados.items():
    if grado > max_grado:
        max_grado = grado
        planeta_mas_conectado = planeta

# 5. Encontrar la ruta más larga (arista con mayor distancia)
ruta_mas_larga = None
max_distancia = 0
# Recorremos todas las aristas evitando duplicados
for planeta in sistema_solar:
    for vecino, distancia in sistema_solar[planeta]:
        if distancia > max_distancia:
            max_distancia = distancia
            ruta_mas_larga = (planeta, vecino, distancia)

# 6. Crear arrays de NumPy en el mismo orden de las claves
planetas = list(sistema_solar.keys())
grados_array = np.array(list(grados.values()))
distancias_array = np.array(list(distancias_totales.values()))

# 7. Imprimir resultados en consola
print("Array de rutas por planeta:", grados_array)
print("Array de distancias acumuladas por planeta:", distancias_array)
print(f"Planeta más conectado: {planeta_mas_conectado} con {max_grado} rutas")
print(f"Ruta más larga: {ruta_mas_larga[0]} - {ruta_mas_larga[1]} con {ruta_mas_larga[2]} unidades")

# 8. Gráfico de barras para cantidad de rutas
plt.bar(planetas, grados_array, color="purple")
plt.title("Cantidad de rutas por planeta")
plt.xlabel("Planeta")
plt.ylabel("Número de rutas")
plt.grid(axis='y', linestyle='--')
plt.show()

# 9. Gráfico de barras para distancias acumuladas
plt.bar(planetas, distancias_array, color="green")
plt.title("Distancia total conectada por planeta")
plt.xlabel("Planeta")
plt.ylabel("Distancia acumulada")
plt.grid(axis='y', linestyle='--')
plt.show()