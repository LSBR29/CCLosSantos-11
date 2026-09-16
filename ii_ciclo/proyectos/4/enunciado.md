# Proyecto 4

# Lista de Tareas

## Descripción

En este proyecto se desarrollará una aplicación de consola en C++ para administrar una lista de tareas.

Para este proyecto se utilizará Git y GitHub, o sea, el programa debe ir evolucionando mediante diferentes cambios registrados en el historial del repositorio.

---

## Enunciado

Desarrolle un programa que permita administrar una lista de tareas mediante un menú interactivo.

Cada tarea deberá almacenar la siguiente información:

* Nombre o descripción de la tarea.
* Estado de la tarea.

El programa deberá mantener las tareas utilizando un `vector`.

El menú principal deberá incluir las siguientes opciones:

```text
LISTA DE TAREAS

1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Marcar tarea como completada
5. Salir

Seleccione una opción:
```

---

## Funcionalidades

### 1. Agregar tarea

Solicite al usuario una descripción para la nueva tarea y agréguela a la lista.

Toda tarea va a comenzar con el estado:

```text
Pendiente
```

Por ejemplo:

```text
Ingrese la tarea: Estudiar para el examen

Tarea agregada correctamente.
```

---

### 2. Mostrar tareas

Recorra el `vector` y muestre todas las tareas registradas.

Cada tarea deberá indicar su estado.

Por ejemplo:

```text
TAREAS

1. [Pendiente] Estudiar para el examen
2. [Completada] Entregar proyecto
3. [Pendiente] Leer documentación de Git

```

---

### 3. Marcar tarea como completada

Muestre las tareas disponibles y solicite el número de la tarea que desea marcar como completada.

Si la tarea existe, cambie su estado:

```text
Pendiente
```

a:

```text
Completada
```

Por ejemplo:

```text
Seleccione la tarea: 1

Tarea marcada como completada.
```

Si la tarea no existe, deberá mostrarse un mensaje indicando que la opción no es válida.

---

### 4. Salir

Finaliza la ejecución del programa.

---

## Estructuras de datos requeridas

El programa deberá utilizar una estructura para representar una tarea.

Puede utilizar:

```cpp
struct Tarea {
    string descripcion;
    bool completada;
};
```

Todas las tareas deberán almacenarse utilizando:

```cpp
vector<Tarea>
```

---

## Funciones obligatorias

El programa deberá estar organizado mediante funciones. Puede utilizar:

```cpp
// Agrega una nueva tarea al vector
void agregarTarea(vector<Tarea>& tareas);

// Muestra todas las tareas
void mostrarTareas(const vector<Tarea>& tareas);

// Marca una tarea como completada
void completarTarea(vector<Tarea>& tareas);
```

El menú principal deberá utilizar estas funciones para realizar las diferentes operaciones.

---

## Desarrollo utilizando Git y GitHub

Este proyecto deberá desarrollarse utilizando un repositorio de GitHub.

El desarrollo deberá realizarse progresivamente mediante diferentes commits.

Como mínimo, el historial deberá contener cambios equivalentes a los siguientes:

### Versión 1 — Proyecto inicial

Crear la estructura básica del programa, el menú y la opción para agregar tareas.

---

### Versión 2 — Mostrar tareas

Agregar la funcionalidad para mostrar las tareas almacenadas.

---

### Versión 3 — Completar tareas

Agregar la posibilidad de marcar una tarea como completada.

--- 

## Uso de una rama

Después de completar las funcionalidades principales del proyecto, deberá desarrollar una mejora adicional sin modificar directamente la rama principal.

La funcionalidad será:

### Prioridad de las tareas

Agregue a cada tarea una prioridad:

```text
Alta
Media
Baja
```

Por ejemplo:

```text
1. [Pendiente] [Alta] Estudiar para el examen
2. [Pendiente] [Media] Entregar proyecto
3. [Completada] [Baja] Organizar archivos
```

La mejora deberá desarrollarse utilizando una rama independiente.

---

### 1. Crear la rama

Ingrese al repositorio del proyecto en GitHub.

En la página principal del repositorio, localice el selector de ramas, donde normalmente aparecerá:

```text
main
```

Seleccione el selector y escriba el nombre de la nueva rama:

```text
feature/prioridades
```

GitHub mostrará una opción similar a:

```text
Create branch: feature/prioridades
```

Seleccione esa opción.

**Importante:** todos los cambios relacionados con la nueva funcionalidad deberán realizarse en `feature/prioridades`.

---

### 2. Trabajar dentro de la rama

Antes de modificar cualquier archivo, compruebe que el selector de ramas muestra:

```text
feature/prioridades
```

Realice los cambios necesarios en el código para agregar la prioridad a cada tarea.

La información de cada tarea deberá permitir almacenar:

* descripción.
* estado.
* prioridad.

Por ejemplo, una tarea podría representarse como:

```text
[Pendiente] [Alta] Estudiar para el examen
```

También deberá modificar las partes necesarias del programa para que la prioridad pueda mostrarse correctamente.

---

### 3. Guardar los cambios mediante un commit

Una vez completada la funcionalidad, realice un commit.

---

### 4. Crear la Pull Request

Una vez que la funcionalidad esté terminada deberá crear una Pull Request para proponer que los cambios de la rama se incorporen a `main`.

Desde la página principal del repositorio, seleccione:

```text
Pull requests
```

Después seleccione:

```text
New pull request
```

GitHub mostrará dos ramas.

Configure:

```text
base:
main
```

y:

```text
compare:
feature/prioridades
```

---

### 5. Completar la Pull Request

Asigne un título.

En la descripción explique brevemente qué se modificó.

Después seleccione:

```text
Create pull request
```

---

### 6. Revisar los cambios

GitHub mostrará los archivos modificados y las diferencias entre:

```text
main
```

y:

```text
feature/prioridades
```

Revise que:

* los cambios correspondan únicamente a la funcionalidad nueva.
* no se hayan eliminado partes del proyecto accidentalmente.
* el programa mantenga las funcionalidades anteriores.
* la nueva funcionalidad esté implementada correctamente.

---

### 7. Integrar la rama

Una vez revisada la Pull Request, seleccione:

```text
Merge pull request
```

y posteriormente confirme:

```text
Confirm merge
```

Los cambios de:

```text
feature/prioridades
```

pasarán a formar parte de:

```text
main
```