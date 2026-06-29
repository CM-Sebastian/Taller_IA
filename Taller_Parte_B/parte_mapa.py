from pathlib import Path
from src.grid_search import load_grid_from_file, bfs_grid, dfs_grid, astar_grid, render_grid_with_path

BASE_DIR = Path(__file__).resolve().parents[1]

grid  = load_grid_from_file(str(BASE_DIR / "Taller_Parte_B" / "taller_data" / "el_mapa_del_tesoro.txt"))
def mostrar_resultado(name, grid, path):
    print(f"-----{name}-----")
    print("Camino:", path)
    print("Longitud:", len(path))
    print(render_grid_with_path(grid,path))

mostrar_resultado("BFS", grid, bfs_grid(grid))

mostrar_resultado("A*", grid, astar_grid(grid))