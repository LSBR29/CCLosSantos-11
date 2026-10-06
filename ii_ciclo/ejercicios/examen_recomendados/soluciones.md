# Soluciones de los Ejercicios Recomendados

### 1.
**Respuesta:**
- Línea 5: `int edad = "15";` debe ser `int edad = 15;`
- Línea 6: falta el `;` al final de `double altura = 1.75`
- Línea 7: `Verdadero` no existe en C++, debe ser `true`

Una vez corregido, el programa imprime `15 1.75 1`.

---

### 2.
**Respuesta:** En la línea 12 se escribe `titulo` sin indicar a qué variable pertenece. Se corrige con `libro.titulo = "El tunel";`. Una vez corregido, el programa imprime `El tunel: 144 paginas`.

---

### 3.
**Respuesta:** El parámetro `const Libro& l` no permite modificar el objeto, y la línea 11 intenta cambiar `l.paginas`. Si la función debe modificarlo, se quita `const`: `void reiniciar(Libro& l)`. Con ese cambio el programa imprime `El tunel: 0 paginas`.

**Explicación:**

`const &` evita copiar el objeto y además prohíbe modificarlo, por lo que sirve para funciones que solo leen. Cuando la función debe cambiar el original, el parámetro se declara con `&` y sin `const`.

---

### 4.
**Respuesta:** Imprime `3 8`, pero debería imprimir `8 3`. Se corrige escribiendo los parámetros por referencia: `void intercambiar(int& a, int& b)`.

**Explicación:**

Con `int a, int b` la función recibe copias de `x` y `y`. El intercambio ocurre dentro de las copias y las variables originales no cambian. Con `&` la función trabaja directamente sobre `x` y `y`.

---

### 5.
**Respuesta:** `25 25 99`

**Explicación:**

`b` es una referencia a `a`: son dos nombres para la misma variable, por eso `b = 25` también cambia `a`. En cambio `int c = a;` crea una copia con el valor actual (25). Después, `c = 99` solo cambia la copia.

---

### 6.
**Respuesta:** Imprime `Quedan 0`, pero debería imprimir `Quedan 3`. Se corrige cambiando la condición a `intentos == 0`.

**Explicación:**

El operador `=` asigna: `intentos = 0` guarda un 0 en la variable, y el valor de esa expresión (0) se interpreta como falso, por lo que se ejecuta el `else`, cuando `intentos` ya vale 0. Para comparar se usa `==`. El código compila sin error, aunque algunos compiladores muestran una advertencia en esa línea.

---

### 7.
**Respuesta:** Imprime `8 1`. El promedio debería ser `8.33333`. Se corrige dividiendo entre `3.0`.

**Explicación:**

La suma es 25 y `25 / 3` es una división entre dos enteros, así que el resultado también es entero (8). Ese 8 recién después se guarda en el `double`. Con `3.0` uno de los operandos tiene decimales y el resultado conserva los decimales. El operador `%` devuelve el residuo de la división, que es 1.

---

### 8.
**Respuesta:** Imprime `4`, pero debería imprimir `15`. Se corrige quitando el `return total;` que está dentro del ciclo.

**Explicación:**

`return` termina la función en el momento en que se ejecuta. En la primera vuelta del ciclo solo se ha sumado `4.0` y la función ya devuelve ese valor. El `return` debe estar después del ciclo, para que se sumen todos los elementos antes de devolver el resultado.

---

### 9.
**Respuesta:**
```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Consumo {
    string mes;
    double litros;
};

// Devuelve el promedio de litros de todos los meses
double calcularPromedio(const vector<Consumo>& consumos) {
    double suma = 0;
    for (int i = 0; i < consumos.size(); i++) {
        suma += consumos[i].litros;
    }
    return suma / consumos.size();
}

// Devuelve el nombre del mes con mayor consumo
string mesMayorConsumo(const vector<Consumo>& consumos) {
    int posicionMayor = 0;
    for (int i = 1; i < consumos.size(); i++) {
        if (consumos[i].litros > consumos[posicionMayor].litros) {
            posicionMayor = i;
        }
    }
    return consumos[posicionMayor].mes;
}

int main() {
    vector<Consumo> consumos = {
        {"Enero", 12500.0},
        {"Febrero", 9800.0},
        {"Marzo", 14200.0},
        {"Abril", 11000.0}
    };

    cout << "Promedio: " << calcularPromedio(consumos) << endl;
    cout << "Mayor consumo: " << mesMayorConsumo(consumos) << endl;

    return 0;
}
```

---

### 10.
**Respuesta:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Devuelve la tarifa a pagar segun las horas de parqueo
int calcularTarifa(int horas) {
    int tarifa;
    if (horas <= 2) {
        tarifa = horas * 1000;
    } else {
        tarifa = 2 * 1000 + (horas - 2) * 800;
    }

    if (tarifa > 5000) {
        tarifa = 5000;
    }
    return tarifa;
}

int main() {
    vector<int> horas = {1, 3, 6, 10};
    int total = 0;

    for (int i = 0; i < horas.size(); i++) {
        int tarifa = calcularTarifa(horas[i]);
        cout << "Horas: " << horas[i] << " -> " << tarifa << endl;
        total += tarifa;
    }

    cout << "Total: " << total << endl;

    return 0;
}
```
