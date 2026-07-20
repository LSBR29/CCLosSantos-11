# II Examen
## Indicaciones generales
- La duración del examen es de 2h.
- Subir la solución al Google Classroom en el espacio denominado *II Examen*.
    - En caso de problemas, puede enviar la solución al correo [santiagobrenesruiz@gmail.com](mailto:santiagobrenesruiz@gmail.com)
- Debe entregar el archivo: `main.py`.
- El examen es de carácter individual.
- Es permitido utilizar una hoja de apuntes o notas.

---

# Grados de amistad en una red social
Existe una idea conocida como los **grados de separación**, la cual plantea que cualquier persona puede conectarse con otra a través de una pequeña cadena de conocidos, muchas veces se habla de aproximadamente **7 grados de separación** entre personas.

Las redes sociales pueden representarse utilizando **grafos**:
* Cada persona corresponde a un **nodo**.
* Cada amistad corresponde a una **arista**.
* Las amistades son mutuas, por lo que el grafo es **no dirigido**.

## Estructura de amistades
Se va a trabajar con una red social formada por exactamente las siguientes conexiones:

| Persona | Amistades |
| ------- | --------- |
| A       | B, C      |
| B       | A, C, E   |
| C       | A, B, D   |
| D       | C         |
| E       | B         |

Las letras anteriores son únicamente etiquetas, usted debe elegir los nombres de las personas, puede utilizar cualquier temática (no necesariamente tiene que usar nombres reales).

## Funcionamiento esperado
1. Representar la red usando una lista de adyacencia.
2. Calcular el grado de cada nodo.
3. Almacenar los grados usando NumPy.
4. Visualizar los resultados mediante un gráfico de barras.

---

## Por implementar
### Representación del grafo
Debe crear un grafo donde:
* Cada nodo represente una persona y las aristas sus amistades.

La estructura debe respetar exactamente las conexiones indicadas.

### Extracción de nombres
Debe obtener una lista con los nombres de las personas.

### Cálculo de grados
Debe recorrer el grafo, calcular el grado de cada persona y guardarlo en una lista.
El grado corresponde a:
* La cantidad de amistades que tiene un nodo.

### Obtención de amigos promedio
Debe obtener el promedio de grados según la lista creada en el paso anterior.
Puede usar la función:
* sum(lista) : para sumar todos los elementos de una lista

### Creación del array de NumPy
Debe crear un `np.array` con la lista que contiene los grados calculados.

### Generación del gráfico
Debe generar un gráfico de barras usando `matplotlib`.

El gráfico debe incluir:
* Nombres de las personas en el eje X.
* Cantidad de amistades en el eje Y.
* Un título.
* Cuadrícula horizontal utilizando:

  ```python
  plt.grid(axis='y')
  ```

### Mostrar resultados
Debe imprimir en consola el nombre de las personas, el promedio de amigos y el array de numpy.

---

## Criterios de evaluación
**Representación del grafo**
- Uso correcto de diccionario con conjuntos (`set`): 25 pts
**Procesamiento**
- Extracción correcta de nombres: 10 pts
- Cálculo correcto de grados: 15 pts
- Cálculo correcto del promedio de amigos: 15 pts
- Conversión correcta a `np.array`: 10 pts
**Visualización**
- Gráfico completo con todos los elementos: 20 pts
**Código**
- Código ordenado, comentado y con nombres claros: 5 pts
**Total: 100 pts**

---

# Puntos extra (+6 puntos)
Realice un dibujo a mano del grafo.

## Requisitos
- Debe incluir:
  - Todos los nodos
  - Todas las conexiones
  - Los mismos nombres utilizados en el código

## Entrega
Debe tomar una foto y subirlo como imagen junto con el archivo `.py`.