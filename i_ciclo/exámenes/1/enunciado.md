# I Examen
## Indicaciones generales
- La duración del examen es de 2h.
- Subir al Google Classroom las soluciones en el espacio denominado *I Examen*.
    - En caso de tener problemas puede enviar la solución al correo santiagobrenesruiz@gmail.com
- Debe entregar el archivo: `main.py`.
- El examen es de carácter individual.
- Es permitido utilizar una hoja notas o apuntes.

---

## Construcción de un árbol con comandos
Se debe completar un programa que procese una lista de comandos para construir un árbol binario.

El archivo `main.py` ya tiene código desarrollado el cual no es necesario modificar (`class Nodo`, `imprimirArbol` y el bloque `if __name__ == "__main__"`), puede encontrarlo en Classroom.

### Comandos a implementar
| Comando      | Significado |
|--------------|-------------|
| `ADD x`      | Agrega un nodo con valor `x` en el árbol. |
| `IZQ`        | Indica que el próximo `ADD` debe insertarse como el **descendiente más a la izquierda** del nodo actual. |
| `DER`        | Indica que el próximo `ADD` debe insertarse como el **descendiente más a la derecha** del nodo actual. |

### Funcionameinto
1. **Primer `ADD x`**: crea la raíz del árbol.
2. **Dirección**: los comandos `IZQ` y `DER` determinan la forma de inserción para el **siguiente** `ADD`.
3. **Agregar nodo (`ADD x`)**:
   - Si hay una dirección pendiente (`IZQ` o `DER`), se inserta el nuevo nodo siguiendo esa dirección hasta encontrar un lugar vacío (el hijo izquierdo o derecho más profundo según corresponda).
   - Se asume que al inicio la dirección pendiente es `None` y por ello está creando la raíz, luego asuma que siempre habrá una dirección pendiente.
   - El nuevo nodo se almacena en una pila (lista) de nodos.

### Por implementar
- **`nuevoIzq(nodoActual, nuevoNodo)`**: inserta `nuevoNodo` como el descendiente más a la izquierda del árbol. Recorre recursivamente por los hijos izquierdos hasta encontrar un nodo sin hijo izquierdo y allí lo coloca.
- **`nuevoDer(nodoActual, nuevoNodo)`**: inserta `nuevoNodo` como el descendiente más a la derecha del árbol. Recorre recursivamente por los hijos derechos hasta encontrar un nodo sin hijo derecho y allí lo coloca.
- **`construir(comandos)`**:
  - Procesa los comandos en orden como si se tratase de una cola.
  - Mantiene una variable que recuerda la dirección pendiente (`"IZQ"`, `"DER"` o `None`).
  - Cada vez que aparece `ADD x`, crea un nodo con valor `x`:
    - Si no hay dirección pendiente se guarda en la pila (lista) de nodos y se toma como la raíz.
    - Si hay dirección pendiente, llama a la función correspondiente (`nuevoIzq` o `nuevoDer`) pasándole la raíz y el nuevo nodo a añadir.
  - Devuelve la raíz del árbol.

### Ejemplo de ejecución
Con la lista de comandos dada, la salida debe ser:
```
        -> 15
    -> 7
-> 10
    -> 5
        -> 3
```

---

## Criterios de evaluación
**Funciones**
- `nuevoIzq` implementada correctamente (recursión, inserción al final): 20 pts
- `nuevoDer` implementada correctamente (recursión, inserción al final): 20 pts
**Comandos**
- Manejo de comandos como cola: 10 pts
- Manejo correcto de la dirección pendiente (`IZQ`/`DER`): 15 pts
- Creación correcta de nodos: 15 pts
- Almacenamiento de los nodos: 10 pts
- Función devuelve el resultado esperado: 5pts
**Código**
- Código ordenado, nombres de variables claras y comentarios: 5 pts
**Total** **100 pts**