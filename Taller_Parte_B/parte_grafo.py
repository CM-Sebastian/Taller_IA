from src.graph_search import bfs,dfs

el_grafo = {
        "A": ["E"],
        "B": ["F"],
        "C": ["A","E"],
        "D": ["B"],
        "E": ["D","F"],
        "F": ["B"],
}

print("---BFS del grafo:---\n",bfs(el_grafo, "C", "B", debug=True))
print("---DFS del grafo:---\n",dfs(el_grafo, "C", "B", debug=True))
