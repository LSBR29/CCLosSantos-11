import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el grafo dirigido de depredación
# Cada especie caza a las que están en su conjunto
ecosistema = {
    "Águila": {"Conejo", "Serpiente", "Ratón"},
    "Zorro": {"Conejo", "Ratón"},
    "Serpiente": {"Ratón", "Lagartija"},
    "Búho": {"Ratón", "Lagartija", "Serpiente"},
    "Conejo": {"Hierba"},
    "Ratón": {"Semillas"},
    "Lagartija": {"Insectos"}
}

# 2. Calcular cantidad de presas de cada especie (grado de salida)
n_presas = {}
for especie in ecosistema:
    n_presas[especie] = len(ecosistema[especie])

# 3. Calcular cantidad de depredadores de cada especie (grado de entrada)
# Inicializar contador en 0 para todas las especies
n_depredadores = {}

# Recorrer cada especie y sus presas
for presas_set in ecosistema.values():
    for presa in presas_set:
        # Si la presa existe en el diccionario
        if presa in n_depredadores:
            n_depredadores[presa] += 1
        else:
            n_depredadores[presa] = 0

# 4. Encontrar superdepredador (más presas)
superdepredador = None
max_presas = 0
for especie, cantidad in n_presas.items():
    if cantidad > max_presas:
        max_presas = cantidad
        superdepredador = especie

# 5. Encontrar especie más vulnerable (más depredadores)
vulnerable = None
max_depredadores = 0
for especie, cantidad in n_depredadores.items():
    if cantidad > max_depredadores:
        max_depredadores = cantidad
        vulnerable = especie

# 6. Crear arrays de NumPy en el mismo orden de las especies
especies = list(ecosistema.keys())
presas_array = np.array(list(n_presas.values()))
depredadores_array = np.array(list(n_depredadores.values()))

# 7. Imprimir resultados
print("Array de presas:", presas_array)
print("Array de depredadores:", depredadores_array)
print(f"Superdepredador: {superdepredador} con {max_presas} presas")
print(f"Especie más vulnerable: {vulnerable} con {max_depredadores} depredadores")

# 8. Gráfico de barras para presas
plt.bar(especies, presas_array, color="green")
plt.title("Cantidad de presas")
plt.xlabel("Especie")
plt.ylabel("Número de presas")
plt.grid(axis='y', linestyle='--')
plt.show()

# 9. Gráfico de barras para depredadores
plt.bar(especies, depredadores_array, color="red")
plt.title("Cantidad de depredadores")
plt.xlabel("Especie")
plt.ylabel("Número de depredadores")
plt.grid(axis='y', linestyle='--')
plt.show()