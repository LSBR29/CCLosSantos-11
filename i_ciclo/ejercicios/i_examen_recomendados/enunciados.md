# Ejercicios Recomendados

---
## 1. Insertar a los extremos de un árbol
Implemente la función:
```python
def insertar_extremo(nodo, nuevo, direccion):
```

La función debe:
* Recibir un nodo inicial (raíz del árbol).
* Recibir un nuevo nodo a insertar.
* Recibir una dirección (`"izquierda"` o `"derecha"`).

Comportamiento:
* Si la dirección es `"izquierda"`, debe recorrer recursivamente por los hijos izquierdos hasta encontrar el primer espacio vacío y colocar el nodo ahí.
* Si la dirección es `"derecha"`, debe hacer lo mismo pero hacia la derecha.

**Ejemplo de ejecución**
```python
if __name__ == "__main__":
  raiz = Nodo(10)

  insertar_extremo(raiz, Nodo(5), "izquierda")
  insertar_extremo(raiz, Nodo(3), "izquierda")
  insertar_extremo(raiz, Nodo(20), "derecha")
```

**Salida esperada:**
```
Árbol:
    -> 20
-> 10
    -> 5
        -> 3
```

---
## 2. Procesar instrucciones
Dada una lista de instrucciones como:
```python
["SUMA", "5", "MULT", "3", "SUMA", "2"]
```

Implemente un programa que:
* Procese las instrucciones en orden como si fueran una cola.
* Tenga un valor inicial de 0.
* Aplique cada operación según corresponda:
  * `"SUMA"`: suma el siguiente número
  * `"MULT"`: multiplica por el siguiente número

**Salida esperada:**
```
(((0 + 5) * 3) + 2)
Resultado: 17
```

---
## 3. Operar sobre una pila
Dada una lista de instrucciones como:
```python
["MODO_A", "ACCION", "ACCION", "MODO_E", "ACCION", "MODO_A", "ACCION"]
```

Implemente un programa que:
* Procese las instrucciones en orden como si fueran una cola.
* Mantenga un estado actual (`"MODO_A"` o `"MODO_E"`).

Comportamiento:
* `"MODO_A"`: cambia el estado a modo A
* `"MODO_E"`: cambia el estado a modo B
* `"ACCION"`:
  * Si el estado es `"MODO_A"` : agregar un 1 a la pila
  * Si el estado es `"MODO_E"` : eliminar el último elemento de la pila
  * Siempre imprime la pila

**Salida esperada:**

```
[1]
[1, 1]
[1]
[1, 1]
```

---

### 4. Profundidad de un valor
Implemente la función:
```python
def profundidad(nodo, valor, nivel=0):
```

La función debe:
* Recibir la raíz del árbol.
* Recibir un valor a buscar.
* Retornar el nivel (profundidad) en el que se encuentra ese valor.

Reglas:
* La raíz se encuentra en el nivel 0.
* Si el valor no existe en el árbol, debe retornar `-1`.

**Salida esperada:**
```
Árbol:
        10
       /  \
      5    15
     / \
    3   7

Profundidad de 10: 0
Profundidad de 7: 2
Profundidad de 15: 1
Profundidad de 8: -1
```