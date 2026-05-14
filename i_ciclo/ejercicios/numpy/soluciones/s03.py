import numpy as np

temp_max = np.array([22, 24, 19, 27, 30, 28, 26, 23, 25, 31, 29, 27, 26, 24, 22])

booleano = temp_max > 28
calurosos = temp_max[booleano]

print(f"Días calurosos: {booleano}")
print(f"Temperaturas de días calurosos: {calurosos}")