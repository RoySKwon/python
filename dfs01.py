# dfs01
# DFS use Recursive function 

def dfs(graph, v, visited):
    visited[v] = True;
    print(v, end=' ');

    for i in graph[v]:
        if not visited[i]:
            print(i, visited);
            dfs(graph, i, visited);

graph = [ [] for _ in range(9)];
# print(graph);

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7],
]

# visited = [ [False] for _ in range(9)];
visited = [False] * 9;
# print(visited);

dfs(graph, 1, visited);
