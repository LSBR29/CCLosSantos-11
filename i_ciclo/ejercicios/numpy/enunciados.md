# Ejercicios NumPy

### 1. Control de inventario en un almacén

Un almacén tiene 5 productos diferentes. Las cantidades actuales en inventario están dadas por el siguiente array:

```python
inventario = np.array([120, 45, 78, 200, 33])
```

Hoy llegaron las siguientes cantidades adicionales:

```python
llegadas = np.array([10, 5, 0, 30, 7])
```

Utilice numpy para actualizar el inventario sumando las llegadas. Luego, identificar qué productos tienen menos de 50 unidades y mostrar sus cantidades.

**Salida esperada:**
```
Inventario actualizado: [130  50  78 230  40]
Productos con menos de 50 unidades: [40]
```

### 2. Notas de estudiantes

Las notas de 8 estudiantes en un examen son:

```python
notas = np.array([68, 72, 100, 90, 55, 83, 79, 61])
```

Se decide aplicar una curva: sumar 5 puntos a todas las notas, pero sin que ninguna supere 100.

Utilice numpy para sumar 5 y luego limitar las notas a máximo 100. Además, cuente cuántos estudiantes aprobaron (nota ≥ 60).

**Salida esperada:**
```
Notas corregidas: [73 77 100 95 60 88 84 66]
Cantidad de aprobados: 8
```

### 3. Temperaturas diarias

Se registraron las temperaturas máximas (°C) durante 15 días:

```python
temp_max = np.array([22, 24, 19, 27, 30, 28, 26, 23, 25, 31, 29, 27, 26, 24, 22])
```

Un día se considera caluroso si la temperatura supera los 28°C.

Utilice numpy para obtener un array booleano que indique qué días fueron calurosos. Luego, usando indexación booleana, extraiga las temperaturas exactas de esos días calurosos y mostrarlas.

**Salida esperada:**
```
Días calurosos: [False False False False  True False False False False  True  True False False False False]
Temperaturas de días calurosos: [30 31 29]
```

### 4. Mapa de un parqueo

Se tiene un parqueo representado por una matriz de 6 filas x 6 columnas. Los valores representan: `0` = lugar vacío, `1` = lugar ocupado.

```python
parqueo = np.array([
    [0,1,0,0,1,1],
    [1,1,0,0,0,1],
    [0,0,0,1,0,0],
    [1,0,1,0,1,0],
    [0,1,0,0,0,0],
    [1,1,0,0,1,1]
])
```

Utilice numpy para encontrar las coordenadas (fila, columna) de todos los lugares vacíos (`0`). Y luego muestre la cantidad total de lugares vacíos.

**Salida esperada:**
```
(Filas: [0 0 0 1 1 1 2 2 2 2 2 3 3 3 4 4 4 4 4 5 5], Columnas: [0 2 3 2 3 4 0 1 2 4 5 1 3 5 0 2 3 4 5 2 3])
Cantidad de lugares vacíos: 21
```

### 5. Ajuste de precios por inflación

Los precios de 10 productos en una tienda son:

```python
precios = np.array([1200, 550, 890, 2300, 450, 990, 1750, 320, 680, 1250])
```

La inflación aplica un aumento del 8% a todos los productos. Sin embargo, los productos que cuestan menos de 500 colones suben un 12% en lugar del 8%.

Utilice numpy para aplicar los aumentos correspondientes. Muestre los precios finales como numeros enteros.

**Salida esperada:**
```
Precios finales: [1296  594  961 2484  504 1069 1890  358  734 1350]
```

### 6. Detección de píxeles

Una imagen en blanco y negro se representa como una matriz 10x10, donde cada valor es un entero entre 0 (negro) y 255 (blanco). Se proporciona la siguiente matriz:

```python
imagen = np.array([
    [120, 30, 45, 200, 210, 89, 67, 255, 140, 100],
    [55, 90, 210, 230, 40, 30, 25, 180, 190, 60],
    [80, 70, 130, 180, 210, 50, 40, 30, 20, 110],
    [210, 220, 90, 80, 70, 200, 210, 85, 45, 35],
    [30, 45, 60, 200, 210, 220, 130, 90, 100, 110],
    [200, 190, 45, 35, 40, 210, 220, 70, 80, 90],
    [100, 110, 120, 50, 45, 60, 200, 210, 220, 130],
    [35, 40, 50, 210, 220, 100, 90, 80, 70, 200],
    [210, 200, 190, 60, 70, 130, 140, 150, 45, 40],
    [50, 60, 70, 200, 190, 180, 45, 35, 30, 200]
])
```

Utilice numpy para determinar cuántos píxeles son considerados "oscuros" (valor < 80). Luego, cree una nueva matriz donde esos píxeles oscuros se conviertan a 0 y los demás se mantengan igual.

**Salida esperada:**
```
Cantidad de píxeles oscuros: 40
Nueva imagen:
[[120   0   0 200 210  89   0 255 140 100]
 [  0  90 210 230   0   0   0 180 190   0]
 [ 80   0 130 180 210   0   0   0   0 110]
 [210 220  90  80   0 200 210  85   0   0]
 [  0   0   0 200 210 220 130  90 100 110]
 [200 190   0   0   0 210 220   0  80  90]
 [100 110 120   0   0   0 200 210 220 130]
 [  0   0   0 210 220 100  90  80   0 200]
 [210 200 190   0   0 130 140 150   0   0]
 [  0   0   0 200 190 180   0   0   0 200]]
```

### 7. Conversión de temperaturas

Se tiene un array con temperaturas en grados Celsius:

```python
celsius = np.array([0, 10, 20, 30, 37, 40, 100])
```

Utilice numpy para convertir todas las temperaturas a Fahrenheit usando la fórmula `F = C * 9/5 + 32`. Luego, usando comparaciones y `np.where()`, cree un nuevo array que indique si cada temperatura en Fahrenheit es mayor a 90°F (poner `"caliente"`) o no (`"frio"`).

**Salida esperada:**
```
Temperaturas en Fahrenheit: [ 32.  50.  68.  86.  98.6 104.  212. ]
Clasificación: ['frio' 'frio' 'frio' 'frio' 'caliente' 'caliente' 'caliente']
```

### 8. Simulación de lanzamiento de monedas

Se lanzó una moneda 20 veces y se registró 1 para cara y 0 para escudo, obteniendo:

```python
lanzamientos = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0])
```

Con numpy:

a) Cuente cuántas caras (1) hubo.

b) Use `np.where()`, para cambiar todos los valores 1 por el string `"Cara"` y todos los 0 por `"Escudo"`.

c) Muestre el array resultante.

**Salida esperada:**
```
Cantidad de caras: 11
Resultado del lanzamiento:
['Cara' 'Escudo' 'Cara' 'Cara' 'Escudo' 'Escudo' 'Cara' 'Escudo' 'Cara'
 'Cara' 'Cara' 'Escudo' 'Escudo' 'Cara' 'Escudo' 'Cara' 'Escudo' 'Cara'
 'Cara' 'Escudo']
```