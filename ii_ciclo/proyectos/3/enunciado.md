# Proyecto 3
# Analizador de Sensores

## Descripción

En este proyecto se desarrollará una aplicación de consola en C+* para analizar información obtenida de diferentes sensores.

El programa deberá leer las mediciones almacenadas en un archivo de texto, guardar la información utilizando un `vector` y permitir realizar diferentes consultas sobre los datos utilizando estructuras de la biblioteca estándar de C++.

---

## Enunciado

Desarrolle un programa que analice un archivo de datos de sensores. El archivo se llama:

```text
sensores.txt
```

Cada línea del archivo representa una medición de un sensor y contiene la siguiente información, separada por comas:

```text
sensor,temperatura,voltaje
```

Por ejemplo:

```text
S1,24.5,120.1
S2,26.7,119.8
S1,25.1,120.2
S3,31.4,118.9
S2,27.2,121.0
```

El programa deberá leer el archivo, almacenar todas las mediciones y presentar un menú con las siguientes opciones:

```text
ANALIZADOR DE SENSORES

1. Mostrar mediciones
2. Mostrar información por sensor
3. Mostrar mayores temperaturas
4. Salir

Seleccione una opción:
```

---

## Funcionalidades

### 1. Leer el archivo

Al iniciar, el programa debe:

1. Intentar abrir el archivo `sensores.txt`.

2. Si no se puede abrir, mostrar:

   ```text
   Error: No se pudo abrir el archivo sensores.txt
   ```

3. Si se abre correctamente, leer el archivo línea por línea:

   * Separar los campos utilizando la coma (`,`) como delimitador.
   * Convertir `temperatura` y `voltaje` a números decimales.
   * Crear una estructura `Medicion` con esos datos.
   * Agregar cada medición al `vector`.

---

### 2. Mostrar mediciones

Recorra el `vector` de mediciones y muestre todos los datos almacenados.

Por ejemplo:

```text
MEDICIONES

Sensor: S1
Temperatura: 24.5 °C
Voltaje: 120.1 V
-----------------------------

Sensor: S2
Temperatura: 26.7 °C
Voltaje: 119.8 V
-----------------------------

Sensor: S1
Temperatura: 25.1 °C
Voltaje: 120.2 V
-----------------------------
```

---

### 3. Mostrar información por sensor

El programa deberá mostrar la cantidad de sensores diferentes y la cantidad de mediciones realizadas por cada sensor.

#### 3.1 Sensores diferentes

Obtenga los sensores diferentes que aparecen en el archivo.

Por ejemplo, si el archivo contiene mediciones de `S1`, `S2`, `S1`, `S3` y `S2`, deberá identificarse que existen tres sensores diferentes.

La salida deberá mostrar:

```text
SENSORES REGISTRADOS

Cantidad de sensores: 3
```

---

#### 3.2 Mediciones por sensor

Cuente y muestre la cantidad de mediciones correspondientes a cada sensor.

Por ejemplo:

```text
MEDICIONES POR SENSOR

S1: 2
S2: 2
S3: 1
```

---

### 4. Mostrar mayores temperaturas

Ordene las mediciones de mayor a menor temperatura.

Después de ordenarlas, muestre las cinco mediciones con mayor temperatura.

Por ejemplo:

```text
MAYORES TEMPERATURAS

1. S3 - 34.2 °C
2. S1 - 33.8 °C
3. S4 - 32.9 °C
4. S2 - 32.5 °C
5. S3 - 32.1 °C
```

---

### 5. Salir

Finaliza la ejecución del programa.

---

## Estructuras de datos requeridas

El programa debe utilizar la siguiente estructura:

```cpp
struct Medicion {
    string sensor;
    double temperatura;
    double voltaje;
};
```

---

## Funciones obligatorias

El programa deberá estar organizado mediante funciones. Como mínimo, debe completar:

```cpp
// Lee el archivo y retorna un vector con las mediciones
vector<Medicion> leerArchivo();

// Muestra todas las mediciones
void mostrarMediciones(...);

// Muestra la cantidad de sensores diferentes y las mediciones correspondientes a cada sensor
void mostrarInformacionPorSensor(...);

// Ordena las mediciones por temperatura y muestra las cinco temperaturas más altas
void mostrarMayoresTemperaturas(...);
```

---

## Función adicional

Además de las funcionalidades anteriores, deberá implementar **una función adicional** de la siguiente lista.

La función será asignada aleatoriamente a cada estudiante.

| Version | Función               | Descripción                                                 |
| ------- | --------------------- | ----------------------------------------------------------- |
| A       | `promedioTemperatura` | Calcula el promedio de temperatura de todas las mediciones. |
| B       | `promedioVoltaje`     | Calcula el promedio de voltaje de todas las mediciones.     |

Todas las funciones deberán utilizar la siguiente estructura:

```cpp
double funcion(const vector<Medicion>& mediciones);
```

La función adicional deberá utilizar las mediciones que ya fueron cargadas desde el archivo.

Esta función es independiente de las opciones del menú.

---

## Ejemplo

Archivo `sensores.txt`:

```text
S1,24.5,120.1
S2,26.7,119.8
S1,25.1,120.2
S3,31.4,118.9
S2,27.2,121.0
```

Ejecución del programa:

```text
ANALIZADOR DE SENSORES

1. Mostrar mediciones
2. Mostrar información por sensor
3. Mostrar mayores temperaturas
4. Salir

Seleccione una opción: 2

SENSORES REGISTRADOS

Cantidad de sensores: 3

MEDICIONES POR SENSOR

S1: 2
S2: 2
S3: 1
```

Posteriormente:

```text
Seleccione una opción: 3

MAYORES TEMPERATURAS

1. S3 - 31.4 °C
2. S2 - 27.2 °C
3. S2 - 26.7 °C
4. S1 - 25.1 °C
5. S1 - 24.5 °C
```
