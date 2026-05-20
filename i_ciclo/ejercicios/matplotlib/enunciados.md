# Ejercicios Matplotlib

### 1. Estilos diferentes

Escriba un programa que grafique dos o más líneas en una misma figura utilizando diferentes estilos de línea, colores y marcadores.

Puede usar:
```python
x = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [2, 4, 6, 8, 10, 12, 14, 16]
y2 = [1, 4, 9, 16, 25, 36, 49, 64]
```

**Salida esperada:**
Una gráfica con varias líneas, leyenda, título y etiquetas en los ejes.

### 2. Gráfico de dispersión

Escriba un programa que:

* Genere valores aleatorios para `X` y `Y`.
* Dibuje un gráfico de dispersión usando círculos vacíos como marcadores.

**Salida esperada:**
Una nube de puntos con círculos sin relleno.

### 3. Gráfico de líneas a partir de un archivo de texto

Se dispone de un archivo `test.txt` que contiene pares de números separados por espacios.

Ejemplo:

```txt
1 2
2 4
3 1
```

Escriba un programa que:

* Lea el archivo y extraiga los valores de `x` y `y`.
* Dibuje una gráfica de líneas usando esos puntos.

**Salida esperada:**
Una gráfica de líneas construida a partir de los datos del archivo.

### 4. Difusin de calor

Escriba un programa que:

1. Cree una matriz de `15×15` llena de ceros.
2. Colocar un valor de `100` en el centro de la matriz.
3. Actualizar la matriz durante `10` pasos de tiempo.
4. En cada paso:

   * cada celda interna debe calcularse como el promedio entre:

     * la celda actual,
     * la celda superior,
     * la celda inferior,
     * la celda izquierda,
     * la celda derecha.
5. Mostrar la matriz en cada iteración usando:

   * `imshow()`
   * un mapa de color tipo `"hot"`
   * un título indicando el tiempo actual.

**Salida esperada:**
Una secuencia de imágenes que muestre cómo el calor se difunde desde el centro.

### 5. Propagación de un incendio forestal

Utilice los siguientes estados para celdas en una matriz:

* `0`: suelo vacío
* `1`: árbol sano
* `2`: árbol en fuego
* `3`: ceniza

Escriba un programa que:

1. Cree una matriz aleatoria de `25×25`:

   * `80%` árboles,
   * `20%` suelo vacío.
2. Inicie un incendio en la posición `(1,1)`.
3. En cada paso de la simulación:

   * un árbol sano se incendia si alguno de sus vecinos (arriba, abajo, izquierda o derecha) está en fuego,
   * un árbol en fuego se convierte en ceniza.
4. Ejecute la simulación mientras existan árboles en fuego.
5. Muestre la matriz en cada paso utilizando:

   * `imshow()`
   * un mapa de colores personalizado.

**Salida esperada:**
Una secuencia de imágenes que muestre la propagación del incendio.

### 6. Simulación de epidemia

Utilice los siguientes valores para representar el estado de una persona:

* `0`: sano
* `1`: infectado
* `2`: recuperado

Escriba un programa que:

1. Cree una matriz aleatoria de `20×20`:

   * `99%` personas sanas,
   * `1%` personas infectadas.
2. Simule `15` pasos de tiempo.
3. En cada paso:

   * una persona sana se infecta si alguno de sus vecinos (arriba, abajo, izquierda o derecha) está infectado,
   * una persona infectada se recupera en el siguiente paso.
4. Muestre la matriz en cada iteración utilizando:

   * `imshow()`
   * un mapa de colores personalizado.

**Salida esperada:**
Una secuencia de imágenes que muestre la propagación de la enfermedad.

### 7. Recorrido de un laberinto

Utilice los siguientes valores para representar cada celda:

* `0`: espacio vacío
* `1`: pared
* `2`: espacio rellenado

Escriba un programa que:

1. Cree una matriz que represente un pequeño laberinto.
2. Seleccione una posición inicial para comenzar el relleno.
3. En cada paso:

   * una celda vacía se rellena si alguno de sus vecinos (arriba, abajo, izquierda o derecha) ya está rellenado.
4. Ejecute la simulación hasta que ya no existan nuevas celdas para rellenar.
5. Muestre la matriz en cada iteración utilizando:

   * `imshow()`
   * un mapa de colores personalizado.

**Matriz de ejemplo**
```python
matriz = np.array([
   [1,1,1,1,1,1,1,1,1,1],
   [1,0,0,0,1,0,0,0,0,1],
   [1,0,1,0,1,0,1,1,0,1],
   [1,0,1,0,0,0,0,1,0,1],
   [1,0,1,1,1,1,0,1,0,1],
   [1,0,0,0,0,1,0,1,0,1],
   [1,1,1,1,0,1,0,1,0,1],
   [1,0,0,1,0,0,0,1,0,1],
   [1,0,0,0,0,1,0,0,0,1],
   [1,1,1,1,1,1,1,1,1,1]
])
```

**Salida esperada:**
Una secuencia de imágenes donde el relleno se expande progresivamente por la región conectada.