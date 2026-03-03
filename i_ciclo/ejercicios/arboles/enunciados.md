# Ejercicios Árboles

Puede asumir una estructura básica de un árbol como:
```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
```

### 1. Contar nodos y hojas

Dado un **árbol binario**, cree funciones que permitan:
* Contar el total de nodos.
* Contar la cantidad de hojas.
* Calcular la altura del árbol.

Cada función debe recibir como parámetro la raíz del árbol.

**Salida esperada:**

```
Árbol:
        10
       /  \
      5    15
     / \
    3   7

Total de nodos: 5
Total de hojas: 3
Altura: 2
```

### 2. Buscar un valor

Implemente la función:

```python
def buscar(nodo, valor):
```

La función debe:

* Retornar `True` si el valor existe en el árbol.
* Retornar `False` si no existe.

**Salida esperada:**

```
Árbol:
        10
       /  \
      5    15
     / \
    3   7

Buscar 3: True
Buscar 9: False
```

### 3. Verificar si dos árboles son iguales

Dados dos árboles binarios, cree una función que determine si son iguales.

Dos árboles son iguales si:
* Tienen la misma estructura.
* Tienen los mismos valores en cada posición correspondiente.

**Salida esperada:**

```
Árbol A:
        4
       / \
      2   6

Árbol B:
        4
       / \
      2   6

Árbol C:
        4
       / \
      2   7

Iguales A y B: True
Iguales A y C: False
```

### 4. Ruta con suma objetivo

Dado un árbol binario donde cada nodo contiene un número entero, cree una función que determine si existe **un camino desde la raíz hasta una hoja** cuya suma de valores sea igual a un número objetivo dado.

Cree la función:

```python
def existe_camino_suma(nodo, objetivo):
```

La función debe:

* Retornar `True` si existe al menos un camino cuya suma sea igual al objetivo.
* Retornar `False` en caso contrario.

**Salida esperada:**

```
Árbol:
        5
       / \
      4   8
     /   / \
    11  13   4
   /  \
  7    2

Objetivo 22: True
Objetivo 26: True
Objetivo 19: False
```

### 5. Subárbol dentro de otro árbol

Dados dos árboles binarios:

* Árbol principal A
* Árbol B

Determine si el árbol B aparece dentro del árbol A como un subárbol.

Cree la función:

```python
def es_subarbol(A, B):
```

Debe retornar:

* `True` si existe algún nodo en A cuya estructura completa sea idéntica a B.
* `False` en caso contrario.

*Puede ser útil la solución del problema 3*

**Salida esperada:**

```
Árbol A:
        3
       / \
      4   5
     / \
    1   2

Árbol B:
      4
     / \
    1   2

Árbol C:
      4
     / \
    1   3

B subárbol de A: True
C subárbol de A: False
```
