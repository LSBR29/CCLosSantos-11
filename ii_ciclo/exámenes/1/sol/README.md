Nombre: Solución

| Línea | Justificación | Corrección |
|---|---|---|
| 8 | Falta el `;` después de la llave que cierra el `struct` | `};` |
| 10 | El parámetro se pasa por valor, la función modifica una copia y `a` no cambia | `void sumarPuntos(Jugador& j, int extra) {` |
| 22 | Las comillas dobles crean un texto, un `char` se escribe con comillas simples | `char inicial = 'A';` |
| 25 | `Jugador&` crea una referencia (otro nombre para `a`) y no un respaldo | `Jugador respaldo = a;` |
| 29 | `>` no realiza la comparación | `if (a.puntos >= 100) {` |