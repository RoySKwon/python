# bfs01

from collections import deque;

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7],
];

print(graph);

def bfs(graph, start, visited):
    queue = deque([start]); #start value with deque lib
    visited[start] = True; # now Node

    while queue: # while empty gueue
        v = queue.popleft(); # pop
        print(v, end = ' ');

        for i in graph[v]: # related Nodes
            if not visited[i]:
                queue.append(i);
                visited[i] = True;

visited = [False] * 9;

bfs(graph, 1, visited);
