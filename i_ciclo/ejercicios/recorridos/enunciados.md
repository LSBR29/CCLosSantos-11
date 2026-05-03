## Ejercicios de Recorridos
### 1. Computadoras conectadas

Dado un **grafo no dirigido**, donde cada nodo representa una computadora y cada arista representa conexión directa, cree una función que permita:

* Listar todas las computadoras alcanzables desde una computadora inicial.

La función debe recibir como parámetros el grafo y la computadora inicial.

**Salida esperada:**

```
Grafo:
A -- B      C -- D
             |
             E

Computadora inicial: A
Computadoras alcanzables: ['A', 'B']
```

### 2. Rutas entre ciudades

Dado un **grafo no dirigido**, donde cada nodo representa una ciudad y cada arista representa una carretera, cree una función que permita:

* Encontrar **todas las rutas posibles** desde una ciudad inicial hasta una ciudad destino **sin repetir ciudades**.

La función debe recibir como parámetros el grafo, la ciudad inicial y la ciudad destino.

**Salida esperada:**

```
Grafo:
A -- B -- C
|    |
D ----

Ciudad inicial: A
Ciudad destino: C
Rutas posibles: [['A', 'D', 'B', 'C'], ['A', 'B', 'C']]
```

### 3. Estaciones eléctricas

Dado un **grafo no dirigido**, donde cada nodo representa una estación eléctrica y cada arista representa una conexión, cree una función que permita:

* Encontrar todos los caminos desde una estación inicial hasta una final cuya longitud (cantidad de nodos) sea exactamente ( k ).

La función debe recibir como parámetros el grafo, la estación inicial, la estación final y el valor ( k ).

**Salida esperada:**

```
Grafo:
A -- B -- C
|    |
D ----

Inicio: A
Fin: C
k: 3
Caminos válidos: [['A', 'B', 'C']]
```

### 4. Conexión entre personas

Dado un **grafo no dirigido**, donde cada nodo representa una persona y cada arista representa amistad, cree una función que permita:

* Determinar la **distancia mínima (en número de conexiones)** desde una persona inicial hacia todas las demás.

La función debe recibir como parámetros el grafo y la persona inicial.

**Salida esperada:**

```
Grafo:
A -- B -- C
     |
     D

Personas inicial: A
Distancias: {'A': 0, 'B': 1, 'C': 2, 'D': 2}
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
Orden de propagación: A, B, D, C  //  A, B, C, D
```

### 6. Número de islas

Dado un **grafo no dirigido**, donde cada nodo representa una isla y cada arista representa que dos islas están conectadas, cree una función que permita:

* Determinar cuántos grupos de islas conectadas existen.

La función debe recibir como parámetro el grafo.

**Salida esperada:**

```
Grafo:
A -- B      C -- D
             |
             E

Número de grupos: 2
```