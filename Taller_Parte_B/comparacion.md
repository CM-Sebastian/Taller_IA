# Comparación de los resultados

## 1. Parte del grafo
Aquí el resultado fue el mismo para los dos métodos (BFS y DFS):

![Prueba de BFS y DFS](taller_data\grafo1.png)

| Algoritmo | ¿Encontró camino? | Longitud del camino | Resultado |
|---|---|---:|---|
| BFS | Sí | Igual que DFS | ['C', 'E', 'D', 'B'] |
| DFS | Sí | Igual que BFS | ['C', 'E', 'D', 'B'] |

## 2. Parte del mapa
Aquí, aunque la longitud para llegar a la meta fue la misma, BFS y A* escogieron caminos distintos:

![Prueba de BFS y A*](taller_data\mapa1.png)

| Algoritmo | ¿Encontró camino? | Longitud del camino | Resultado |
|---|---|---:|---|
| BFS | Sí | 19 | Encontró un camino válido (el de arriba) |
| A* | Sí | 19 | Encontró un camino válido (el de abajo) |
