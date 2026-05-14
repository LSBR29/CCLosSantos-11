import numpy as np

parqueo = np.array([
    [0,1,0,0,1,1],
    [1,1,0,0,0,1],
    [0,0,0,1,0,0],
    [1,0,1,0,1,0],
    [0,1,0,0,0,0],
    [1,1,0,0,1,1]
])

vacios = np.where(parqueo == 0)
filas = vacios[0]
columnas = vacios [1]

print(f"(Filas: {filas}, Columnas: {columnas})")
print(f"Cantidad de lugares vacíos: {filas.size}")