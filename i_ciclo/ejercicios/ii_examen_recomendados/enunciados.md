# Ejercicios Recomendados

---

# 1. Sistema de rutas entre ciudades

Una empresa de transporte desea analizar la conexión entre distintas ciudades mediante carreteras.

Cada ciudad tendrá conexiones directas con otras ciudades y se desea estudiar cuáles son las más importantes dentro de la red.

Escriba un programa que:

1. Cree un diccionario donde:

   * cada clave sea una ciudad,
   * y cada valor sea un conjunto (`set`) con las ciudades conectadas directamente.

2. Utilice exactamente `6` ciudades.

3. Calcule:

   * cuántas conexiones tiene cada ciudad,
   * cuál es la ciudad con más conexiones,
   * y el promedio de conexiones de toda la red.

4. Cree un `np.array` con la cantidad de conexiones por ciudad.

5. Genere:

   * un gráfico de barras mostrando las conexiones de cada ciudad,

6. Imprima:

   * el array de NumPy,
   * la ciudad más conectada,
   * y el promedio de conexiones.

---

# 2. Ecosistema de depredadores y presas

En un ecosistema algunos animales cazan a otros para alimentarse.

Cada especie tendrá una lista de animales que puede cazar.

Escriba un programa que:

1. Cree un diccionario donde:

   * cada clave sea una especie,
   * y cada valor sea un conjunto (`set`) con las especies que puede cazar.

2. Utilice exactamente `7` especies diferentes.

3. Calcule:

   * cuántas presas tiene cada especie,
   * cuántos depredadores tiene cada especie,
   * y cuál es el superdepredador (el que más animales caza).

4. Cree dos arrays de NumPy:

   * uno para cantidad de presas,
   * otro para cantidad de depredadores.

5. Genere:

   * un gráfico de barras para presas,
   * y otro gráfico de barras para depredadores.

6. Muestre en consola:

   * ambos arrays,
   * el nombre del superdepredador,
   * y la especie más vulnerable.

---

# 3. Red eléctrica entre estaciones

Una compañía eléctrica desea analizar cómo se conectan distintas estaciones de energía.

Cada estación tendrá conexiones con otras estaciones y cada conexión tendrá un consumo energético asociado.

Escriba un programa que:

1. Cree un diccionario donde:

   * cada clave sea una estación,
   * y cada valor y cada valor sea un conjunto (`set`) con tuplas que contienen:

     * estaciones conectadas,
     * y el consumo energético de cada conexión.

2. Utilice exactamente `5` estaciones eléctricas.

3. Calcule:

   * cuántas conexiones tiene cada estación,
   * el consumo energético total de cada estación,
   * y cuál estación consume más energía.

4. Cree dos arrays de NumPy:

   * uno con cantidad de conexiones,
   * otro con consumo energético total.

5. Genere:

   * un gráfico de barras para conexiones,
   * y otro gráfico para consumo energético.

6. Muestre en consola:

   * ambos arrays,
   * la estación más importante,
   * y el consumo promedio de la red.

---

# 4. Sistema de misiones espaciales

Una agencia espacial desea analizar las rutas de viaje entre distintos planetas.

Cada planeta tendrá rutas hacia otros planetas y cada ruta tendrá una distancia determinada.

Escriba un programa que:

1. Cree un diccionario donde:

   * cada clave sea un planeta,
   * y cada valor y cada valor sea un conjunto (`set`) con tuplas que contienen:

     * planetas conectados,
     * y la distancia de cada ruta.

2. Utilice exactamente `6` planetas.

3. Calcule:

   * cuántas rutas tiene cada planeta,
   * la distancia total conectada a cada planeta,
   * y cuál es el planeta más conectado.

4. Cree dos arrays de NumPy:

   * uno para cantidad de rutas,
   * otro para distancias acumuladas.

5. Genere:

   * un gráfico de barras para rutas,
   * y otro gráfico para distancias.

6. Muestre en consola:

   * ambos arrays,
   * el planeta más conectado,
   * y la ruta más larga.