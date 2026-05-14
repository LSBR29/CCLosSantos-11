import numpy as np

inventario = np.array([120, 45, 78, 200, 33])
llegadas = np.array([10, 5, 0, 30, 7])

actualizado = inventario + llegadas
menos50 = actualizado[actualizado < 50]

print(f"Inventario actualiado: {actualizado}")
print(f"Productos con menos de 50 unidades: {menos50}")