# Proyecto 5

# Minijuego

## Descripción

En este proyecto se desarrollará un pequeño juego gráfico en C++ utilizando `graphics.h`.

El jugador deberá hacer clic sobre diferentes objetivos que aparecerán en distintas posiciones de la pantalla. El objetivo será completar 10 objetivos en el menor tiempo posible.

---

## Enunciado

Desarrolle un programa gráfico que muestre un objetivo en una ventana y permita al usuario interactuar con él utilizando el mouse.

Al iniciar el programa deberá mostrarse el nombre del juego, el objetivo actual y el tiempo.

La pantalla deberá presentar una estructura similar a:

```text
--------------------------------------------------------------
MINIJUEGO                                      Tiempo: 0.00 s
Objetivo: 1/10


                         ■


--------------------------------------------------------------
```

El objetivo deberá aparecer en una posición diferente cada vez que el usuario acierte.

El juego finalizará después de completar 10 objetivos.

---

## Funcionalidades

### 1. Inicializar la ventana gráfica

El programa deberá utilizar `graphics.h` para crear la ventana gráfica.

Deberá mostrar:

* nombre del juego;
* número de objetivo actual;
* tiempo transcurrido;
* objetivo que debe seleccionar el usuario.

---

### 2. Mostrar el objetivo

El objetivo deberá representarse mediante una figura pequeña.

Puede utilizar, por ejemplo:

```cpp
bar(...)
```

Deberá aparecer dentro del área disponible de juego y no deberá colocarse sobre el texto de la interfaz.

---

### 3. Detectar el mouse

El programa deberá obtener continuamente:

* posición horizontal del mouse;
* posición vertical del mouse;
* estado del botón izquierdo.

La lectura del mouse deberá realizarse utilizando las funciones desarrolladas durante la clase.

---

### 4. Detectar un acierto

Cuando el usuario haga clic, el programa deberá comprobar si la posición del mouse se encuentra dentro del objetivo.

Si el clic ocurre fuera del objetivo, el juego deberá continuar sin avanzar al siguiente objetivo.

Si el clic ocurre dentro del objetivo:

1. Se considera el objetivo completado.
2. Se incrementa el contador.
3. Se genera una nueva posición para el siguiente objetivo.

Por ejemplo:

```text
Objetivo: 3/10
```

Después de acertar:

```text
Objetivo: 4/10
```

---

### 5. Generar posiciones aleatorias

Cada nuevo objetivo deberá aparecer en una posición diferente utilizando valores aleatorios.

La posición deberá mantenerse dentro del área visible de juego.

---

### 6. Mostrar el progreso

Durante el juego deberá mostrarse el objetivo actual:

```text
Objetivo: 5/10
```

El contador deberá actualizarse cada vez que el usuario acierte un objetivo.

---

### 7. Cronómetro

El tiempo deberá comenzar únicamente cuando el usuario acierte el primer objetivo.

Antes del primer acierto deberá mostrarse:

```text
Tiempo: 0.00 s
```

Después del primer acierto, el tiempo deberá comenzar a avanzar y mostrarse durante el resto del juego.

Por ejemplo:

```text
Objetivo: 6/10
Tiempo: 4.37 s
```

El cronómetro deberá detenerse cuando el usuario complete el décimo objetivo.

---

### 8. Finalizar el juego

Cuando el usuario complete los 10 objetivos, deberá finalizar el juego y mostrarse una pantalla indicando:

```text
JUEGO TERMINADO

Tiempo: 8.42 segundos
```