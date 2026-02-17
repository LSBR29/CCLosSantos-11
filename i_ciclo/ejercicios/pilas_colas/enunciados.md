# Ejercicios Pilas
### 1. Paréntesis balanceados
Dada una cadena (string) que contiene solo paréntesis `(` y `)`, determinar si están correctamente balanceados.
Cree una función que retorne `True` si está balanceada y `False` si no lo está.

**Salida esperada:**
```
Ingrese la cadena a verificar: (())()
True

Ingrese la cadena a verificar: )(
False
```

### 2. Invertir una cadena
Dada una cadena (string) , crear una función que la invierta usando una pila.

**Salida esperada:**
```
Ingrese la cadena a invertir: hola
aloh
```

### 3. Sistema de escritura
Crear un sistema de escritura estilo menú en la lína de comandos con tres instrucciones posibles:
- escribir `palabra`: añade `palabra` al texto final
- undo: Elimina la última palabra
- salir: Imprime la cadena final

No es necesario que cree una función, puede realizarlo en el main
Puede ser útil la instrucción `texto.startswith(string)`, que devuelve True si `texto` empieza por `string`.

**Salida esperada:**
```
> escribir hola
> escribir mundo
> undo
> escribir prueba
> salir
hola prueba
```

# Ejercicios Colas
### 1. Retrasar elementos
Dada una lista de números (definida en una variable, y que puede tomarse como una cola), en el main hacer que se retrase el primer elemento hacia el final de la lista.

**Salida esperada:**
```
Lista: [1, 2, 3, 4, 5]
2 3 4 5 1

Lista: [10, 20, 30]
20 30 10
```

### 2. Rotación de elementos
Dada una lista de números y un entero k (definir cada uno en una variable), rotar los elementos k posiciones hacia la izquierda usando una cola.
Cree una función que retorne la lista resultante.

**Salida esperada:**
```
Lista: [1, 2, 3, 4, 5]
k: 2
3 4 5 1 2

Lista: [1, 2, 3, 4, 5]
k: 4
5 1 2 3 4
```

### 3. Ventana deslizante
Dada una lista de números y un entero k (definir cada uno en una variable), determine el valor máximo en cada grupo consecutivo de tamaño k, avanzando de izquierda a derecha.
Cree una función que retorne una lista con los máximos encontrados.

**Salida esperada:**
```
Lista: [2, 1, 3, 4, 6, 3, 8, 9, 10, 12, 56]
k: 4
4 6 6 8 9 10 12 56

Lista: [2, 1, 3, 4, 6, 3, 8, 9, 10, 12, 56]
k: 8
9 10 12 56
```

# Ejercicios Colas de Prioridad
### 1. Restar números
Dada una lista de números (definida en una variable), de la manera más eficiente haga una función que efectue los siguientes pasos:
* Se seleccionan los dos números más grandes.
* Se calcula su diferencia.
* Si la diferencia es mayor que 0, vuelve a la colección.
* El proceso continúa hasta que quede un solo número o ninguno.

*Recomendado utilizar un ciclo while*

**Salida esperada:**
```
Números: [2, 7, 4, 1, 8, 1]
Resultado final: 1

Números: [10, 10, 5]
Resultado final: 5
```

# Ejercicios Combinados
### 1. Reorganización por Bloques
Dada una cadena formada por letras minúsculas y el carácter `|`, procesarla con las siguientes reglas:

* Las letras se van acumulando hasta encontrar un `|`.
* Cada vez que aparece un `|`, el bloque de letras leído desde el último`|` debe:
    * Invertirse.
    * Imprimirse más adelante en conjuto con todos los bloques.

* Si al final de la cadena queda un bloque sin cerrar (sin `|` al final), también debe procesarse igual.
* Imprimir todos los bloques invertidos

*Resomendado usar la función para invertir del problema 2 de pilas*

**Salida esperada:**
```
Ingrese cadena: abc|de|fgh|
cbaedhgf

Ingrese cadena: aloh|odnum|nohtyp
holamundopython
```