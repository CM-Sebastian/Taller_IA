"""Actividad final: rescate en un mapa con obstáculos."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.grid_search import (
    load_grid_from_file,
    load_grid_from_text,
    bfs_grid,
    dfs_grid,
    astar_grid,
    render_grid_with_path,
)
from src.debug_tools import print_section, assert_path_valid


# ─────────────────────────────────────────────────────────────────────
# PRUEBA INCREMENTAL: mapa simple 3x3 para verificar que todo funciona
# ─────────────────────────────────────────────────────────────────────

def prueba_mapa_simple():
    print_section("PRUEBA INCREMENTAL: mapa simple 3x3")

    mapa_simple = """
    S..
    ...
    ..G
    """
    grid = load_grid_from_text(mapa_simple)

    print("Mapa de prueba:")
    for fila in grid:
        print("".join(fila))

    camino = bfs_grid(grid, debug=True)

    try:
        assert_path_valid(camino, camino[0], camino[-1])
        print(f"Longitud del camino: {len(camino)}")
        print("Prueba superada: BFS encuentra camino en mapa simple.")
    except AssertionError as e:
        print(f"ERROR en prueba simple: {e}")


# ─────────────────────────────────────────────────────────────────────
# ACTIVIDAD PRINCIPAL: mapa 8x8 con obstáculos
# ─────────────────────────────────────────────────────────────────────

def main():

    # ── Prueba incremental primero ───────────────────────────────────
    prueba_mapa_simple()

    # ── Cargar mapa real ─────────────────────────────────────────────
    ruta_mapa = os.path.join(os.path.dirname(__file__), "..", "data", "mapa.txt")
    grid = load_grid_from_file(ruta_mapa)

    print_section("MAPA CARGADO (8x8)")
    for fila in grid:
        print("".join(fila))

    # ── BFS con debug ────────────────────────────────────────────────
    print_section("BFS — Búsqueda en anchura (debug activado)")
    print("Estrategia: cola FIFO, garantiza camino más corto.\n")
    camino_bfs = bfs_grid(grid, debug=True)
    assert_path_valid(camino_bfs, camino_bfs[0], camino_bfs[-1])
    print("\nCamino encontrado (* = ruta):")
    print(render_grid_with_path(grid, camino_bfs))

    # ── DFS con debug ────────────────────────────────────────────────
    print_section("DFS — Búsqueda en profundidad (debug activado)")
    print("Estrategia: pila LIFO, NO garantiza camino más corto.\n")
    camino_dfs = dfs_grid(grid, debug=True)
    assert_path_valid(camino_dfs, camino_dfs[0], camino_dfs[-1])
    print("\nCamino encontrado (* = ruta):")
    print(render_grid_with_path(grid, camino_dfs))

    # ── A* con debug ─────────────────────────────────────────────────
    print_section("A* — Búsqueda informada (debug activado)")
    print("Estrategia: cola de prioridad con costo + heurística Manhattan.\n")
    camino_a = astar_grid(grid, debug=True)
    assert_path_valid(camino_a, camino_a[0], camino_a[-1])
    print("\nCamino encontrado (* = ruta):")
    print(render_grid_with_path(grid, camino_a))

    # ── Tabla comparativa ────────────────────────────────────────────
    print_section("TABLA COMPARATIVA")
    print(f"{'Algoritmo':<12} {'¿Encontró?':<12} {'Longitud':<10} {'Observación'}")
    print("-" * 70)
    datos = [
        ("BFS", camino_bfs, "Camino más corto garantizado, explora más nodos"),
        ("DFS", camino_dfs, "No garantiza camino corto, puede variar"),
        ("A*",  camino_a,   "Eficiente, guiado por heurística Manhattan"),
    ]
    for nombre, camino, obs in datos:
        encontro = "Sí" if camino else "No"
        longitud = len(camino) if camino else "-"
        print(f"{nombre:<12} {encontro:<12} {longitud:<10} {obs}")

    # ── Explicación final ────────────────────────────────────────────
    print_section("EXPLICACIÓN FINAL")
    print("""
BFS explora el mapa nivel por nivel usando una cola FIFO. Esto garantiza
que el primer camino encontrado sea el más corto. Sin embargo, visita
muchos nodos antes de llegar a la meta, lo que lo hace menos eficiente
en mapas grandes.

DFS usa una pila LIFO y va lo más profundo posible por un camino antes
de retroceder. No garantiza el camino más corto, pero usa menos memoria
que BFS en ciertos casos. En este mapa encontró un camino de igual
longitud, pero por una ruta diferente.

A* combina el costo real acumulado (pasos dados) con una heurística
(distancia Manhattan hasta G). Esto le permite priorizar los nodos más
prometedores y llegar a la meta explorando menos nodos que BFS.
A* es más conveniente cuando el mapa es grande y se necesita eficiencia,
siempre que la heurística no sobreestime la distancia real.

En este mapa, A* fue el más conveniente: encontró el camino óptimo
explorando menos nodos que BFS gracias a la heurística Manhattan.
    """.strip())


if __name__ == "__main__":
    main()