import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el grafo ponderado no dirigido con 5 estaciones
# Cada estación tiene un conjunto de tuplas (estación_vecina, costo_energético)
red_electrica = {
    "A": {("B", 10), ("C", 15), ("D", 20)},
    "B": {("A", 10), ("C", 35), ("E", 25)},
    "C": {("A", 15), ("B", 35), ("D", 30)},
    "D": {("A", 20), ("C", 30), ("E", 40)},
    "E": {("B", 25), ("D", 40)}
}

# 2. Calcular grado (cantidad de conexiones) de cada estación
grados = {}
for estacion in red_electrica:
    grados[estacion] = len(red_electrica[estacion])

# 3. Calcular consumo energético total de cada estación (suma de pesos de sus conexiones)
consumos = {}
for estacion in red_electrica:
    total = 0
    for vecino, costo in red_electrica[estacion]:
        total += costo
    consumos[estacion] = total

# 4. Encontrar la estación que más consume
max_consumo = 0
estacion_max_consumo = None
for estacion, consumo in consumos.items():
    if consumo > max_consumo:
        max_consumo = consumo
        estacion_max_consumo = estacion

# 5. Calcular el consumo promedio de la red (promedio de consumos por estación)
consumo_promedio = sum(consumos.values()) / len(consumos)

# 6. Crear arrays de NumPy en el mismo orden de las claves
estaciones = list(red_electrica.keys())
grados_array = np.array(list(grados.values()))
consumos_array = np.array(list(consumos.values()))

# 7. Imprimir resultados
print("Array de conexiones por estación:", grados_array)
print("Array de consumo energético por estación:", consumos_array)
print(f"Estación con mayor consumo: {estacion_max_consumo} con {max_consumo} unidades")
print(f"Consumo promedio de la red: {consumo_promedio:.2f} unidades")

# 8. Gráfico de barras para conexiones
plt.bar(estaciones, grados_array, color="skyblue")
plt.title("Cantidad de conexiones")
plt.xlabel("Estación")
plt.ylabel("Número de conexiones")
plt.grid(axis='y', linestyle='--')
plt.show()

# 9. Gráfico de barras para consumo energético
plt.bar(estaciones, consumos_array, color="orange")
plt.title("Consumo energético total")
plt.xlabel("Estación")
plt.ylabel("Consumo")
plt.grid(axis='y', linestyle='--')
plt.show()