# Tarea 1
## Descripción  
Esta tarea consiste en desarrollar un programa en python que procese una secuencia de números y la reorganice siguiendo ciertas reglas.
Recuerde incluir **comentarios claros** y **nombres de variables descriptivos** en su solución.

---

## Enunciado
Desarrolle un programa que reciba una secuencia cualquiera de números enteros separando cada elemento por un espacio en blanco:

Por ejemplo:
```
* 1 2 3 4 5 6
* 8 9 10 11
* 2 4 6 8
```

Y luego reciba un número entero positivo `k` menor al tamaño de la secuencia ingresada. En caso de incumplir las condiciones para este número, imprima un mensaje de error y utilice `exit()` u otro método para detener el programa.

Una vez almacenadas la secuencia y el número `k`, efectue los siguientes pasos utilizando únicamente pilas y colas.
  1. Extraer los **primeros** `k` elementos.
  2. **Invertir** el orden de esos `k` elementos.
  3. Mantener el resto de los elementos en el mismo orden original.
  4. Regresar los elementos invertidos o generar una nueva secuencia como resultado final.

---

## Ejemplo  
Entrada:
```python
Secuencia: 1 2 3 4 5 6
Valor de k: 3
```

Proceso:
* Se toman los primeros 3 elementos: `[1, 2, 3]`
* Se reorganizan invirtiendo su orden: `[3, 2, 1]`
* El resto permanece igual: `[4, 5, 6]`
* Resultado final:

Salida:
```python
[3, 2, 1, 4, 5, 6]
```

---

## Restricciones
* No se permite utilizar slicing (`lista[:k]`, `lista[::-1]`, etc.).
* No se permite utilizar funciones que inviertan listas directamente (`reverse()`).
* Solo se pueden utilizar operaciones propias de pilas y colas (push, pull o enqueue, dequeue).

---

## Criterios de Evaluación
- **Uso correcto de operaciones de colas cuando sea necesario (20%)**
- **Uso correcto de operaciones de pilas cuando sea necesario (20%)**
- **Lógica implementada correctamente (25%)**
- **Solicitud de la secuencia (10%)**
- **Solicitud y validación de k (10%)**
- **Cumplimiento de las restricciones (10%)**
- **Cometarios (5%)**