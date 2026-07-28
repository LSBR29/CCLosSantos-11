# Proyecto 1
# Sistema de Gestión de Películas

## Descripción

En este proyecto se desarrollará una aplicación de consola en **C++** para administrar un catálogo de películas.

---

## Enunciado

Desarrolle un programa que permita administrar un catálogo de películas mediante un menú interactivo.

Cada película deberá almacenar la siguiente información:

- Código (entero positivo)
- Nombre
- Género
- Duración (minutos)
- Calificación (entre 0 y 10)

El menú principal deberá repetirse hasta que el usuario decida salir del programa.

Como mínimo deberá incluir las siguientes opciones:

```
Sistema de Gestión de Películas

1. Registrar película
2. Mostrar catálogo
3. Buscar película
4. Modificar película
5. Eliminar película
6. Mostrar estadísticas
7. Salir

Seleccione una opción:
```

---

## Funcionalidades

### 1. Registrar película

Solicite todos los datos de la película y agréguela al catálogo.

Antes de registrar una nueva película debe verificarse que el código no exista previamente.

En caso de existir un código repetido, se deberá mostrar un mensaje indicando el problema y cancelar el registro.

Además, deberá validar que:

- El código sea positivo.
- La duración sea mayor que cero.
- La calificación esté entre 0 y 10.

---

### 2. Mostrar catálogo

Recorra el catálogo e imprima toda la información almacenada para cada película.

Si no existen películas registradas, deberá mostrarse un mensaje indicándolo.

Por ejemplo:

```
Código: 101
Nombre: Interestelar
Género: Ciencia ficción
Duración: 169 minutos
Calificación: 8.7
-----------------------------
Código: 205
Nombre: WALL-E
Género: Animación
Duración: 103 minutos
Calificación: 8.4
-----------------------------
```

---

### 3. Buscar película

Solicite el código de una película.

Si la película existe, deberá mostrarse toda su información.

Si el código no se encuentra registrado, deberá mostrarse un mensaje indicándolo.

---

### 4. Modificar película

Solicite el código de la película que desea modificar.

Si existe, permita actualizar:

- nombre;
- género;
- duración;
- calificación.

El código de la película no podrá modificarse.

Si la película no existe, deberá mostrarse un mensaje indicando el problema.

---

### 5. Eliminar película

Solicite el código de la película.

Si la película existe, elimínela del catálogo.

Si el código no existe, informe al usuario.

---

### 6. Mostrar estadísticas

Recorra el catálogo y muestre la siguiente información:

- Cantidad total de películas registradas.
- Promedio de calificaciones.

Si el catálogo está vacío, deberá indicarse mediante un mensaje.

---

### 7. Salir

Finaliza la ejecución del programa.

---

## Ejemplo

```
Sistema de Gestión de Películas

1. Registrar película
2. Mostrar catálogo
3. Buscar película
4. Modificar película
5. Eliminar película
6. Mostrar estadísticas
7. Salir

Seleccione una opción: 1

Código: 101
Nombre: Interestelar
Género: Ciencia ficción
Duración: 169 minutos
Calificación: 8.7

Película registrada correctamente.
```

Posteriormente:

```
Seleccione una opción: 6

Cantidad de películas: 5
Calificación promedio: 8.74
```

---

## Restricciones

- No debe crear una variable independiente para cada película ingresada.
- El programa deberá estar organizado mediante funciones.
- El menú deberá repetirse hasta seleccionar la opción **Salir**.
- Todas las entradas del usuario deberán validarse cuando corresponda.