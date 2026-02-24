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

*Recomendado usar la función para invertir del problema 2 de pilas*

**Salida esperada:**
```
Ingrese cadena: abc|de|fgh|
cbaedhgf

Ingrese cadena: aloh|odnum|nohtyp
holamundopython
```

### 2. Procesador Matemático
Crear un sistema que reciba diferentes comandos e imprima el resultado al final:
- `NUM x`: agrega un número a la expresión actual
- `SUM`: suma los últimos dos números
- `MUL`: multiplica los últimos dos números

Cuando aparece `SUM` o `MUL`, se toman los últimos dos números, se opera y se vuelve a insertar el resultado a la expresión.

*Recomendado manejar los comandos como una cola (procesarlos conforme llegan) y los números guardarlos en una pila*

**Salida esperada:**
```
NUM 5
NUM 3
SUM
NUM 2
MUL

RESULTADO: 16
```

### 3. Verificación de secuencia
Dada una secuencia de números enteros, ingresados manualmente y separados por espacio en blanco, cree y utilice las siguientes estructuras para verificar si es posible reorganizarla para obtener la secuencia ordenada creciente (`1, 2, 3, ..., n`):
* Una cola de entrada: Secuencia ingresada
* Una pila auxiliar: Para guardar los números durante el intento de orden
* Una cola de salida: Para ir ordenando los números

Cumpliendo las siguientes reglas:

Solo se puede:
- Tomar el primer elemento de la cola de entrada.
- Moverlo directamente a la cola de salida si es el siguiente número esperado.
- O moverlo a la pila auxiliar para guardarlo.

Desde la pila auxiliar solo se puede:
- Sacar el elemento superior (último elemento) y enviarlo a la cola de salida si es el siguiente número esperado.

**Salida esperada:**
```
Secuencia de entrada: 3 1 2
Sí es posible ordenarla en [1, 2, 3]
```

**Proceso interno**
Se convierte `3 1 2` en la cola de entrada:
```
Cola de entrada: [3, 1, 2]
Pila auxiliar: []
Cola de salida: []
```

Se toma el primer elemento y al ser un `3` se mueve a la pila auxiliar:
```
Cola de entrada: [1, 2]
Pila auxiliar: [3]
Cola de salida: []
```

Se toma el siguiente elemento de la entrada, y al ser un `1` se mueve a la cola de salida.
```
Cola de entrada: [2]
Pila auxiliar: [3]
Cola de salida: [1]
```

Como el `2` está en la entrada se toma y se mueve a la salida:
```
Cola de entrada: []
Pila auxiliar: [3]
Cola de salida: [1, 2]
```

Como el `3` está en la pila auxiliar se toma y se mueve a la salida:
```
Cola de entrada: []
Pila auxiliar: []
Cola de salida: [1, 2, 3]
```

Si es posible ordenar la secuencia.