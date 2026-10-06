# Ejercicios Recomendados

### 1.
El siguiente programa no compila. Encuentre los 3 errores de compilación y corríjalos.
```cpp
#include <iostream>
using namespace std;

int main() {
    int edad = "15";
    double altura = 1.75
    bool mayor = Verdadero;

    cout << edad << " " << altura << " " << mayor << endl;
    return 0;
}
```

---

### 2.
El siguiente programa no compila. El compilador muestra el mensaje `'titulo' was not declared in this scope`. ¿Cuál es el error y cómo se corrige?
```cpp
#include <iostream>
#include <string>
using namespace std;

struct Libro {
    string titulo;
    int paginas;
};

int main() {
    Libro libro;
    titulo = "El tunel";
    libro.paginas = 144;

    cout << libro.titulo << ": " << libro.paginas << " paginas" << endl;
    return 0;
}
```

---

### 3.
El siguiente programa no compila. El compilador muestra el mensaje `assignment of member 'Libro::paginas' in read-only object`. ¿Por qué ocurre y cómo se corrige si la función sí debe modificar el libro?
```cpp
#include <iostream>
#include <string>
using namespace std;

struct Libro {
    string titulo;
    int paginas;
};

void reiniciar(const Libro& l) {
    l.paginas = 0;
}

int main() {
    Libro libro;
    libro.titulo = "El tunel";
    libro.paginas = 144;
    
    reiniciar(libro);

    cout << libro.titulo << ": " << libro.paginas << " paginas" << endl;
    return 0;
}
```

---

### 4.
¿Qué imprime el siguiente código? ¿Qué debería imprimir y cómo se corrige?
```cpp
#include <iostream>
using namespace std;

void intercambiar(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 3;
    int y = 8;

    intercambiar(x, y);

    cout << x << " " << y << endl;
    return 0;
}
```

---

### 5.
¿Qué imprime el siguiente código?
```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int& b = a;
    b = 25;

    int c = a;
    c = 99;

    cout << a << " " << b << " " << c << endl;
    return 0;
}
```

---

### 6.
¿Qué imprime el siguiente código? ¿Qué debería imprimir y cómo se corrige?
```cpp
#include <iostream>
using namespace std;

int main() {
    int intentos = 3;

    if (intentos = 0) {
        cout << "Sin intentos" << endl;
    } else {
        cout << "Quedan " << intentos << endl;
    }

    return 0;
}
```

---

### 7.
¿Qué imprime el siguiente código? ¿Qué debería imprimir para el promedio y cómo se corrige?
```cpp
#include <iostream>
using namespace std;

int main() {
    int n1 = 8;
    int n2 = 9;
    int n3 = 8;

    double promedio = (n1 + n2 + n3) / 3;

    cout << promedio << " " << (n1 + n2 + n3) % 3 << endl;
    return 0;
}
```

---

### 8.
¿Qué imprime el siguiente código? ¿Qué debería imprimir y cómo se corrige?
```cpp
#include <iostream>
#include <vector>
using namespace std;

double sumar(const vector<double>& valores) {
    double total = 0;
    for (int i = 0; i < valores.size(); i++) {
        total += valores[i];
        return total;
    }
    return total;
}

int main() {
    vector<double> valores = {4.0, 6.0, 5.0};

    cout << sumar(valores) << endl;
    return 0;
}
```

---

### 9.
Se tienen los consumos de agua de una casa durante cuatro meses. Complete el programa para que calcule el promedio de litros y el nombre del mes con mayor consumo.
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
    return 0;
}

// Devuelve el nombre del mes con mayor consumo
string mesMayorConsumo(const vector<Consumo>& consumos) {
    return "";
}

int main() {
    vector<Consumo> consumos = {
        {"Enero", 12500.0},
        {"Febrero", 9800.0},
        {"Marzo", 14200.0},
        {"Abril", 11000.0}
    };

    // Imprima el promedio y el mes con mayor consumo.

    return 0;
}
```
La salida debe ser:
```
Promedio: 11875
Mayor consumo: Marzo
```

---

### 10.
Un parqueo cobra según las horas que permanece un vehículo, con estas reglas:
- Las primeras 2 horas cuestan 1000 cada una.
- Desde la tercera hora, cada hora adicional cuesta 800.
- La tarifa máxima por vehículo es 5000.

Complete el programa para que calcule la tarifa de cada vehículo y el total recaudado.
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Devuelve la tarifa a pagar segun las horas de parqueo
int calcularTarifa(int horas) {
    return 0;
}

int main() {
    vector<int> horas = {1, 3, 6, 10};

    // Imprima la tarifa de cada vehiculo y el total recaudado.

    return 0;
}
```
La salida debe ser:
```
Horas: 1 -> 1000
Horas: 3 -> 2800
Horas: 6 -> 5000
Horas: 10 -> 5000
Total: 13800
```