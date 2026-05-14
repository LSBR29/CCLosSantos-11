import numpy as np

precios = np.array([1200, 550, 890, 2300, 450, 990, 1750, 320, 680, 1250], float)   # Se coloca array(lista, tipo_dato) para tomar los números como floats

precios[precios > 500] *= 1 + 8/100
precios[precios < 500] *= 1 + 12/100

print(f"Precios finales: {precios.astype(int)}")  # .astype() permite convertir entre tipos de datos en numpy