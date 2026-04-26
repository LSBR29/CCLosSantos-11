## Ejercicios de Recorridos
### 1. Tiempo de propagación
Dado un **grafo no dirigido**, donde cada nodo representa una persona y cada arista representa contacto, cree una función que permita:

* Determinar cuánto tiempo tarda en propagarse una infección, asumiendo que:
  * Un nodo infecta a todos sus vecinos en **1 minuto**.

La función debe recibir como parámetros el grafo y el nodo inicial.

**Salida esperada:**
```
Grafo:
A -- B -- D
     |
     C

Paciente cero: A
Tiempo total de propagación: 2 minutos
```

### 2. Contar caminos
Dado un **grafo no dirigido**, cree una función que permita:

* Contar cuántos caminos distintos existen entre dos nodos, sin repetir nodos en un mismo camino.

La función debe recibir como parámetros el grafo, el nodo origen y el nodo destino.

**Salida esperada:**
```
Grafo:
A -- B -- D
 \   |
  \- C

Origen: A
Destino: D
Cantidad de caminos: 2
```

### 3. Laberinto

Dada una **matriz**, donde:

* `0` representa un camino libre
* `1` representa una pared

Cree una función que permita:

* Determinar si existe un camino desde una posición inicial (x1, y1) hasta una posición final (x2, y2).

La función debe recibir como parámetros la matriz, la posición inicial y la posición final.

**Salida esperada:**

```
Matriz:
0 0 1
1 0 1
0 0 0

Inicio X: 0
Inicio Y: 0
Fin X: 2
Fin Y: 2
Existe camino: True
```

### 4. Número de islas

Dada una **matriz**, donde:

* `1` representa tierra
* `0` representa agua

Cree una función que permita:

* Determinar cuántas islas hay en la matriz.
* Una isla está formada por celdas de tierra conectadas.

La función debe recibir como parámetro la matriz.

**Salida esperada:**

```
Matriz:
1 1 0 0
1 0 0 1
0 0 1 1
0 0 0 0

Número de islas: 3
```

### 5. Noticia

Dado un **grafo no dirigido**, donde cada nodo representa una persona y cada arista representa contacto, cree una función que permita:

* Determinar el orden en que las personas se enteran de una noticia, partiendo de una persona inicial.

La función debe recibir como parámetros el grafo y la persona inicial.

**Salida esperada:**

```
Grafo:
A -- B -- C
     |
     D

Persona inicial: A
Orden de propagación: A, B, D, C   // A, B, C, D
```