import numpy as np

celsius = np.array([0, 10, 20, 30, 37, 40, 100])

fahrenheit = celsius * 9/5 + 32
clasif = np.where(fahrenheit > 90, "caliente", "frio")

print(f"Temperaturas en Fahrenheit: {fahrenheit}")
print(f"Clasificación: {clasif}")