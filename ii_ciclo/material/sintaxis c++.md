# Sintaxis de C++

## Estructura de un programa

Todo programa en C++ necesita una función `main()`. Ese es el punto donde inicia la ejecución.

**Ejemplo:**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hola Mundo";
    return 0;
}
```

| Elemento              | Para qué sirve                                                                |
| --------------------- | ----------------------------------------------------------------------------- |
| `#include <iostream>` | Incluye la biblioteca de entrada y salida (`cout`, `cin`)                     |
| `using namespace std` | Permite escribir `cout` en lugar de `std::cout`                               |
| `int main()`          | Función principal; la ejecución empieza aquí                                  |
| `{ }`                 | Delimitan el cuerpo de un bloque                                              |
| `;`                   | Termina cada instrucción                                                       |
| `return 0;`           | Indica al sistema operativo que el programa terminó sin errores               |

### Comparación con Python

**Python**

```python
print("Hola Mundo")
```

**C++**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hola Mundo";
    return 0;
}
```

### Reglas de escritura

- Cada instrucción termina en `;`
- Los bloques se delimitan con `{ }`, no con indentación
- La indentación **no** afecta la ejecución, pero se mantiene por legibilidad
- Comentarios:

```cpp
// comentario de una línea

/*
comentario
de varias líneas
*/
```

---

## Variables y Tipos de Datos

En Python el tipo se deduce del valor. En C++ el tipo se escribe antes del nombre y **no cambia** durante la ejecución de esa variable.

**Python**

```python
codigo = 15
codigo = "quince"   # válido: la variable cambia de tipo
```

**C++**

```cpp
int codigo = 15;
codigo = "quince";  // error de compilación
```

### Tipos básicos

| Tipo     | Contenido                            | Ejemplo                  | Equivalente en Python |
| -------- | ------------------------------------ | ------------------------ | --------------------- |
| `int`    | Números enteros                      | `int duracion = 169;`    | `int`                 |
| `double` | Números con decimales                | `double calif = 8.7;`    | `float`               |
| `float`  | Decimales con menos precisión        | `float x = 1.5f;`        | —                     |
| `char`   | Un solo carácter, entre comillas `'` | `char letra = 'A';`      | `str` de longitud 1   |
| `bool`   | Verdadero o falso                    | `bool activo = true;`    | `bool`                |
| `string` | Cadena de texto, entre comillas `"`  | `string nombre = "Wall-E";` | `str`              |

Notas:

- `true` y `false` se escriben en minúscula (en Python son `True` y `False`).
- `string` por lo general requiere `#include <string>`.

### Declaración e inicialización

```cpp
int codigo;              // declaración: existe, pero sin valor asignado
codigo = 101;            // asignación

double calificacion = 8.7;   // declaración + inicialización en una línea

int a = 1, b = 2, c = 3;     // varias variables del mismo tipo
```

### Conversión entre tipos

```cpp
int entero = 7;
double decimal = (double) entero;       // De int a double

double nota = 8.7;
int truncada = (int) nota;      // De double a int
```

### División
Si un operando tiene decimales, el resultado también.
Si los dos operandos son enteros, el resultado también.

```cpp
cout << 7 / 2;      // 3
cout << 7.0 / 2;    // 3.5
cout << 7 % 2;      // 1  (residuo)
```

Es el mismo comportamiento que `//` en Python, pero aquí ocurre con el operador `/` normal.

| Operación         | Python  | C++            |
| ----------------- | ------- | -------------- |
| División real     | `7 / 2` | `7.0 / 2`      |
| División entera   | `7 // 2`| `7 / 2`        |
| Residuo           | `7 % 2` | `7 % 2`        |

---

## Operadores

### Aritméticos

```cpp
duracion = duracion + 15;
duracion += 15;          // forma abreviada equivalente
contador++;              // suma 1
contador--;              // resta 1
```

### Relacionales

```cpp
codigo > 0
codigo >= 0
calificacion <= 10
opcion == 7
opcion != 7
```

### Lógicos

| Significado | Python | C++  |
| ----------- | ------ | ---- |
| Y           | `and`  | `&&` |
| O           | `or`   | `\|\|` |
| Negación    | `not`  | `!`  |

---

## Salida de datos

Se usa `cout` junto al operador `<<`, que puede encadenarse.

```cpp
cout << "Nombre: " << nombre << endl;
cout << "Duracion: " << duracion << " minutos" << endl;
```

| Concepto        | Python          | C++                          |
| --------------- | --------------- | ---------------------------- |
| Imprimir texto  | `print("Hola")` | `cout << "Hola";`            |
| Salto de línea  | automático      | `endl` o `"\n"` explícitos   |
| Unir valores    | `print(a, b)`   | `cout << a << b;`            |

---

## Entrada de datos

### `cin`

```cpp
cout << "Codigo: ";
cin >> codigo;

cout << "Duracion: ";
cin >> duracion;
```

`cin >>` convierte el texto al tipo de la variable automáticamente. En Python `input()` devuelve siempre texto y hay que convertirlo.

### El problema del espacio

`cin >>` deja de leer al encontrar un espacio.

**Entrada:**

```text
Prueba String
```

```cpp
string nombre;
cin >> nombre;
cout << nombre;
```

**Salida:**

```text
Prueba
```

### `getline()`

Lee la línea completa, incluidos los espacios.

```cpp
getline(cin, nombre);
```

### El problema del salto de línea

Cuando se usa `cin >>` y después `getline()`, el salto de línea que quedó pendiente en el búfer es leído por `getline()`, que devuelve una cadena vacía.

```cpp
int codigo;
string nombre;

cout << "Codigo: ";
cin >> codigo;

cout << "Nombre: ";
getline(cin, nombre);   // Queda vacío
```

**Entrada:**

```text
101
Interestelar
```

**Salida obtenida:**

```text
Código: 101
Nombre: 

```

La solución es descartar el salto de línea pendiente antes de leer:

```cpp
cout << "Codigo: ";
cin >> codigo;

cin.ignore();

cout << "Nombre: ";
getline(cin, nombre);
```

`cin.ignore()` sin argumentos descarta un carácter del búfer, que en este caso es el salto de línea.

### Cuándo usar cada uno

| Situación                                | Instrucción           |
| ---------------------------------------- | --------------------- |
| Número (`int`, `double`)                  | `cin >> variable;`    |
| Palabra sin espacios                      | `cin >> variable;`    |
| Texto con espacios                        | `getline(cin, variable);` |
| `getline()` inmediatamente después de `cin >>` | `cin.ignore();` antes |

---

## Condicionales

### `if`, `else if`, `else`

**Python**

```python
if opcion == 1:
    print("Registrar")
elif opcion == 2:
    print("Mostrar")
else:
    print("Invalida")
```

**C++**

```cpp
if (opcion == 1) {
    cout << "Registrar";
} else if (opcion == 2) {
    cout << "Mostrar";
} else {
    cout << "Invalida";
}
```

Diferencias:

- La condición va entre paréntesis
- Se usa `else if` en lugar de `elif`
- No hay `:`; el bloque va entre `{ }`

### `switch`

Cuando se compara **una misma variable** contra varios valores fijos, `switch` resulta más legible que una cadena de `if`.

```cpp
switch (opcion) {
    case 1:
        cout << "Registrar pelicula";
        break;
    case 2:
        cout << "Mostrar catalogo";
        break;
    default:
        cout << "Opcion invalida";
        break;
}
```

- Cada `case` compara contra un valor constante
- `break` termina el `switch`; si se omite, la ejecución continúa dentro del siguiente `case`
- `default` cubre cualquier valor no contemplado

---

## Ciclos

### `while`

**Python**

```python
while opcion != 7:
    ...
```

**C++**

```cpp
int opcion = 0;
while (opcion != 7) {
    ...
}
```

### `for` clásico

Declara la variable, indica la condición y el incremento en una sola línea.

```cpp
for (int i = 0; i < 5; i++) {
    cout << i << endl;
}
```

Equivale a:

```python
for i in range(5):
    print(i)
```

| Parte      | Significado                          |
| ---------- | ------------------------------------ |
| `int i = 0`| Se ejecuta una vez, al inicio        |
| `i < 5`    | Se evalúa antes de cada repetición   |
| `i++`      | Se ejecuta al final de cada vuelta   |

## Funciones

```cpp
void mostrarMenu() {
    cout << "Sistema de Gestion de Peliculas\n";
}
```

Llamada:

```cpp
mostrarMenu();
```

Estructura general:

```text
tipo_de_retorno nombre(parametros) { cuerpo }
```

- `void` significa que la función no devuelve ningún valor
- Si devuelve algo, el tipo debe declararse y usarse `return`

```cpp
double promedio(double a, double b) {
    return (a + b) / 2;
}
```

### Paso por valor y por referencia

Por defecto los parámetros se copian; los cambios dentro de la función no afectan a la variable original.

```cpp
void aumentar(int duracion) {
    duracion = duracion + 15;   // solo cambia la copia
}
```

Con `&` la función trabaja sobre la variable original.

```cpp
void aumentar(int &duracion) {
    duracion = duracion + 15;   // cambia la variable original
}
```

---

## Estructuras (`struct`)

Una estructura agrupa varios datos relacionados bajo un solo nombre.

Sin estructura:

```cpp
string nombre1, nombre2, nombre3;
int duracion1, duracion2, duracion3;
```

Con estructura:

```cpp
struct Pelicula {
    int codigo;
    string nombre;
    string genero;
    int duracion;
    double calificacion;
};
```

El `;` después de la llave de cierre es obligatorio.

Uso:

```cpp
Pelicula nueva;

nueva.codigo = 101;
nueva.nombre = "Interestelar";
nueva.duracion = 169;

cout << nueva.nombre;
```

Se accede a cada campo con el punto `.`.

---

## Vectores

Un `vector` es una lista que crece y se reduce durante la ejecución. Requiere `#include <vector>`.

```cpp
#include <vector>

vector<Pelicula> peliculas;   // vector de estructuras
vector<int> numeros;          // vector de enteros
```

Entre `< >` se indica el tipo de los elementos: **todos** los elementos son del mismo tipo, a diferencia de las listas de Python.

### Operaciones básicas

```cpp
Pelicula nueva;
peliculas.push_back(nueva);      // agrega al final

cout << peliculas.size();        // cantidad de elementos

peliculas[0].nombre;             // acceso por índice (empieza en 0)
```

### Recorrido

```cpp
for (int i = 0; i < peliculas.size(); i++) {
    cout << peliculas[i].codigo << endl;
    cout << peliculas[i].nombre << endl;
}
```

### Comparación con listas de Python

| Operación             | Python              | C++                        |
| --------------------- | ------------------- | -------------------------- |
| Crear                 | `lista = []`        | `vector<int> lista;`       |
| Agregar al final      | `lista.append(x)`   | `lista.push_back(x);`      |
| Cantidad              | `len(lista)`        | `lista.size()`             |
| Acceso                | `lista[0]`          | `lista[0]`                 |
| Quitar el último      | `lista.pop()`       | `lista.pop_back();`        |
| Tipos mezclados       | Permitido           | No permitido               |
| Índices negativos     | `lista[-1]`         | No existen                 |

Acceder a una posición inexistente en Python lanza `IndexError`. En C++, `lista[5]` sobre un vector de 2 elementos **no** produce error: es comportamiento indefinido.