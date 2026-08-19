# Proyecto 2
# Sistema de Gestión de Películas: Con Persistencia en Archivo

## Descripción

Este proyecto es una **continuación directa** del **Proyecto 1: Sistema de Gestión de Películas**. Todas las funcionalidades implementadas en el proyecto anterior (registrar, mostrar, buscar, modificar, eliminar y mostrar estadísticas) se conservan exactamente igual, y se les añaden dos nuevas capacidades:

- **Carga inicial de datos** desde un archivo de texto al inicio del programa.
- **Guardado del catálogo** en ese mismo archivo cuando el usuario lo solicite.

---

## Enunciado

Desarrolle un programa que administre un catálogo de películas, utilizando como fuente de datos el archivo:

```text
peliculas.csv
```

Cada línea del archivo representa una película y contiene la siguiente información, separada por comas:

```text
codigo,nombre,genero,duracion,calificacion
```

Por ejemplo:

```text
101,Interestelar,Ciencia Ficcion,169,8.7
102,WALL-E,Animacion,103,8.4
```

Al iniciar, el programa intentará abrir `peliculas.csv`. Si existe, leerá todas las películas y las cargará en un `vector`. Si no existe, mostrará un mensaje informativo y comenzará con el catálogo vacío.

A continuación, se presentará un menú con las mismas opciones del Proyecto 1, más una nueva opción para guardar los cambios en el archivo:

```
Sistema de Gestión de Películas

1. Registrar película
2. Mostrar catálogo
3. Buscar película
4. Modificar película
5. Eliminar película
6. Mostrar estadísticas
7. Guardar catálogo
8. Salir

Seleccione una opción:
```

---

## Funcionalidades nuevas

### Carga inicial (lectura del archivo)

Antes de mostrar el menú, el programa debe:

1. Intentar abrir el archivo `peliculas.csv` en modo lectura.
2. Si no se puede abrir, mostrar:

   ```text
   Archivo peliculas.csv no encontrado. Se iniciará con catálogo vacío.
   ```

3. Si se abre correctamente, leer línea por línea:
   - Separar los campos usando la coma (`,`) como delimitador.
   - Convertir `codigo` y `duracion` a enteros, y `calificacion` a número decimal.
   - Crear una estructura `Pelicula` con esos datos y agregarla al `vector`.

Las líneas mal formadas o vacías se ignoran (no se agregan al catálogo).

---

### Guardar catálogo (opción 7)

Cuando el usuario seleccione esta opción, el programa deberá:

1. Abrir (o crear) el archivo `peliculas.csv` en modo escritura, sobrescribiendo su contenido anterior.
2. Escribir cada película del `vector` en una línea, con el formato:

   ```text
   codigo,nombre,genero,duracion,calificacion
   ```

3. Cerrar el archivo y mostrar el mensaje:

   ```text
   Catálogo guardado correctamente en peliculas.csv.
   ```

Si el `vector` está vacío, el archivo generado debe quedar vacío.

---

## Funcionalidades existentes

Las siguientes opciones se implementaron en el Proyecto 1 y se mantienen idénticas:

- **Registrar película**: solicita código, nombre, género, duración y calificación; valida que el código sea único y que los valores sean correctos.
- **Mostrar catálogo**: imprime todos los datos de cada película en formato legible.
- **Buscar película**: pide un código y muestra la información de esa película si existe.
- **Modificar película**: pide un código y permite actualizar nombre, género, duración y calificación (el código no se modifica).
- **Eliminar película**: pide un código y elimina esa película del catálogo.
- **Mostrar estadísticas**: calcula y muestra la cantidad total de películas y el promedio de calificaciones.

Todas estas operaciones se aplican al `vector` y no afectan el archivo hasta que se ejecute la opción **Guardar**.

---

## Ejemplo

Archivo `peliculas.csv` inicial:

```text
101,Interestelar,Ciencia Ficcion,169,8.7
102,WALL-E,Animacion,103,8.4
```

Ejecución del programa:

```text
Archivo peliculas.csv cargado correctamente.

Sistema de Gestión de Películas

1. Registrar película
2. Mostrar catálogo
3. Buscar película
4. Modificar película
5. Eliminar película
6. Mostrar estadísticas
7. Guardar catálogo
8. Salir

Seleccione una opción: 2

Código: 101
Nombre: Interestelar
Género: Ciencia Ficcion
Duración: 169 minutos
Calificación: 8.7
-----------------------------
Código: 102
Nombre: WALL-E
Género: Animacion
Duración: 103 minutos
Calificación: 8.4
-----------------------------
```

Luego se registra una nueva película:

```text
Seleccione una opción: 1

Código: 103
Nombre: Matrix
Género: Ciencia Ficcion
Duración: 136
Calificación: 8.7

Película registrada correctamente.
```

Se guarda:

```text
Seleccione una opción: 7

Catálogo guardado correctamente en peliculas.csv.
```

El archivo ahora contendrá:

```text
101,Interestelar,Ciencia Ficcion,169,8.7
102,WALL-E,Animacion,103,8.4
103,Matrix,Ciencia Ficcion,136,8.7
```