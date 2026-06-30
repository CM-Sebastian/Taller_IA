# Taller de IA: Algoritmos de Búsqueda (BFS, DFS y A*)

Este repositorio contiene la implementación de los algoritmos de búsqueda para resolver un grafo simple y la navegación de un robot en una cuadrícula con obstáculos.

##  Integrantes y Roles
- **Ashley Lozano:** Mapas y Respuestas de la Parte A.
- **Sebastian Collaguazo:** Parte b
- **Anthony Uribe:** parte c y reflexion final

##  Parte A: Comprensión
1. ¿Por qué BFS encuentra el camino más corto en grafos sin pesos?

Porque explora el mapa por niveles (capa por capa). Primero revisa todos los nodos que están a um paso de distancia del inicio, luego todos los que están a 2 pasos, luego a 3, y así sucesivamente. Como avanza de manera uniforme en todas las direcciones, la primera vez que toca la meta garantiza haber llegado utilizando la menor cantidad de pasos (conexiones) posibles.

2. ¿Por qué DFS puede encontrar una ruta más larga?

Porque DFS no explora por niveles, sino que elige una ruta y se va "a ciegas" por ella hasta el fondo (hasta que se topa con una pared o un camino sin salida) antes de retroceder. Si por casualidad la primera ruta que elige da un rodeo gigantesco por todo el mapa pero finalmente llega a la meta, el algoritmo se detendrá ahí y devolverá ese camino largo, ignorando que quizás a un lado del inicio había un camino directo de solo dos pasos.

3. ¿Qué ventaja tiene A* frente a BFS?

La ventaja principal es la eficiencia guiada (inteligencia).

BFS es "ciego": se expande en forma de círculo perfecto hacia todas las direcciones (arriba, abajo, izquierda, derecha) gastando tiempo y memoria en explorar zonas que están en dirección opuesta a la meta.

A* utiliza una heurística (como la distancia Manhattan), lo que le permite saber en qué dirección general está la meta. De este modo, prioriza explorar los caminos que lo acercan geométricamente al objetivo, ahorrando mucho tiempo y visitando menos casillas innecesarias.

4. ¿Qué ocurre si la heurística sobreestima el costo real?

Si la heurística sobreestima el costo (es decir, le dice al algoritmo que un camino es más largo de lo que realmente es), A pierde la garantía de encontrar el camino más corto. Al sobreestimar, el algoritmo podría esquivar o descartar el camino más corto real pensando erróneamente que es muy costoso, terminando por elegir una ruta más óptima. En Inteligencia Artificial, para que A* sea perfecto, la heurística debe ser admisible (nunca sobreestimar el costo real).

5. ¿Por qué es útil imprimir la frontera durante la depuración?

Es útil por tres razones principales durante el desarrollo:

Verificar el orden de exploración: Te permite confirmar visualmente si estás usando la estructura correcta (si es una cola FIFO para BFS, una pila LIFO para DFS o una cola de prioridad para A*).

Detectar bucles infinitos: Si se nota que la frontera crece sin control con coordenadas repetidas, se sabrá inmediatamente que se olvidó marcar los nodos como "visitados".

Entender el comportamiento: Ayuda a ver en tiempo real hacia dónde se está "inclinando" el robot para buscar y corregir errores antes de que falle el programa completo.

## Mapas de Prueba
Los mapas utilizados para las pruebas están ubicados en la carpeta `data/`:
- `mapa_simple.txt`: Mapa básico sin muchos obstáculos.
- `mapa_obstaculos.txt`: Mapa complejo para probar la eficiencia de A*.
- `mapa8x8.txt`: Mapa general de pruebas.