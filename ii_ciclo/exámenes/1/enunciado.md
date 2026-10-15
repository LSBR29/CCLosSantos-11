# Examen
## Indicaciones generales
- La duración del examen es de 2h 30min.
- Subir al Google Classroom las soluciones en el espacio denominado *Examen*.
    - En caso de tener problemas puede enviar el enlace al correo [santiagobrenesruiz@gmail.com](mailto:santiagobrenesruiz@gmail.com)
- Debe entregar un repositorio de GitHub con los archivos: `README.md` y `main.cpp`.
- En Classroom se encuentran disponibles: `por_corregir.cpp` (Parte 2) y `main.cpp` (Parte 3).
- El examen es de carácter individual.
- Es permitido utilizar una hoja de notas o apuntes.

---

## Parte 1. Creación del repositorio (5 pts)
Se debe crear un repositorio público en GitHub de nombre `examen-cpp` con un `README.md`.

---

## Parte 2. Corrección de código (35 pts)
El siguiente programa tiene 5 errores en líneas distintas, el compilador detecta algunos, otros solo se notan al leer el código y comparar la salida con lo esperado.

El programa debe guardar a Ana con 90 puntos, hacer un respaldo de Ana, sumarle 10 puntos y avisar si llega a 100.

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Jugador {
    string nombre;
    int puntos;
}

void sumarPuntos(Jugador j, int extra) {
    j.puntos += extra;
}

void mostrar(const Jugador& j) {
    cout << j.nombre << ": " << j.puntos << " puntos" << endl;
}

int main() {
    Jugador a;
    a.nombre = "Ana";
    a.puntos = 90;
    char inicial = "A";

    // Respaldo de Ana antes de modificarla
    Jugador& respaldo = a;

    sumarPuntos(a, 10);

    if (a.puntos > 100) {
        cout << "Puntaje maximo" << endl;
    }

    mostrar(a);
    mostrar(respaldo);
    cout << "Inicial: " << inicial << endl;
    return 0;
}
```

### Resultado esperado
Una vez corregido el programa, la salida debe ser:

```
Puntaje maximo
Ana: 100 puntos
Ana: 90 puntos
Inicial: A
```

En GitHub, debe editar el `README.md`, escribir su nombre completo y agregar una tabla con una fila por error, puede usar la siguiente plantilla:

```markdown
Nombre:

| Línea | Justificación | Corrección |
|---|---|---|
|  |  |  |
```

La justificación no tiene que ser extensa. En corrección se escribe el cambio a realizar.

---
## Parte 3. Desarrollo (60 pts)
Se debe completar un programa que calcule el total de una factura con descuento e impuesto. En Classroom tiene un código desarrollado (`struct Producto` y los datos en `main`) el cual no es necesario modificar. 

### Calculos
| Concepto  | Cálculo |
|-----------|---------|
| Subtotal  | Suma de `precio * cantidad` de todos los productos. |
| Descuento | El 10 % del subtotal si el subtotal es mayor que 50000. Si el subtotal es 50000 o menos, el descuento es 0. |
| Base      | Subtotal menos descuento. |
| Impuesto  | El 13 % de la base. |
| Total     | Base más impuesto. |

### Por implementar
- **`calcularSubtotal(productos)`**:
  - Recibe el vector de productos como parámetro.
  - Retorna la suma de `precio * cantidad` de todos los productos.
- **`calcularDescuento(subtotal)`**:
  - Recibe el subtotal como parámetro.
  - Retorna el descuento que corresponde según la regla del cálculo.
- **`calcularImpuesto(base)`**:
  - Recibe la base como parámetro.
  - Retorna el impuesto que corresponde según la regla del cálculo.
- **Función `main`**:
  - Utiliza `calcularDescuento` para obtener el descuento del subtotal.
  - Calcula la base.
  - Utiliza `calcularImpuesto` para obtener el impuesto de la base.
  - Calcula el total.
  - Imprime las líneas `Descuento`, `Impuesto` y `Total`.

### Resultado esperado
Con los datos dados, la salida debe ser:
```
Teclado x2 = 25000
Mouse x3 = 19500
Cable HDMI x4 = 12000
Webcam x1 = 18000
Subtotal: 74500
Descuento: 7450
Impuesto: 8716.5
Total: 75766.5
```

### Entrega en GitHub
Suba el archivo `main.cpp` al mismo repositorio de github, no importa si no funciona por completo.

### Criterios de Evaluación
- `calcularSubtotal` implementada correctamente: 15 pts
- `calcularDescuento` implementada correctamente: 10 pts
- `calcularImpuesto` implementada correctamente: 10 pts
- Cálculo correcto de descuento, base, impuesto y total en `main` utilizando las funciones: 10 pts
- Impresión de las líneas `Descuento`, `Impuesto` y `Total` según el ejemplo: 5 pts
- Archivo `main.cpp` subido al repositorio: 10 pts

**Total: 60 pts**