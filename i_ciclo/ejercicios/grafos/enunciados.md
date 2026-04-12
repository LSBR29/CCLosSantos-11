# Ejercicios Grafos
Utilice listas de adyacencia en todos los ejercicios.

### 1. ¿Están conectados?

Dado un **grafo no dirigido**, cree una función que permita:

* Determinar si existe una **conexión directa** entre dos nodos.

La función debe recibir como parámetros el grafo y los dos nodos a evaluar.

**Salida esperada:**

```
Grafo:
A -- B
|    |
C    D

A - B: True
A - D: False
```

### 2. Nodo más conectado

Dado un **grafo no dirigido**, cree una función que permita:

* Encontrar el nodo con la **mayor cantidad de conexiones** (grado más alto).

La función debe recibir como parámetro el grafo.

**Salida esperada:**

```
Grafo:
A -- B -- C
|    |
D    E

Nodo más conectado: B
Cantidad de conexiones: 3
```

### 3. Red de infección

Dado un **grafo no dirigido**, donde cada nodo representa una persona y cada arista representa contacto, cree una función que permita:

* Determinar cuántas personas se infectan a partir de un **paciente cero**, asumiendo que el virus se propaga a todos los contactos posibles.

La función debe recibir como parámetros el grafo y el nodo inicial (paciente cero).

**Salida esperada:**

```
Grafo:
A -- B -- D    F
     |         |
     C         E

Paciente cero: B
Personas infectadas: 4
```

### 4. Recomendación de amigos

Dado un **grafo no dirigido**, donde cada nodo representa un usuario y cada arista representa una amistad, cree una función que permita:

* Sugerir nuevos amigos a un usuario basado en:

  * Amigos de sus amigos.
  * Excluyendo sus amigos actuales.

La función debe recibir como parámetros el grafo y el usuario.

**Salida esperada:**

```
Grafo:
A -- B -- C
     |
     D

Usuario: A
Amigos actuales: B
Recomendaciones: C, D
```