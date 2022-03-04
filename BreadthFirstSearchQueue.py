# BreadthFirstSearchQueue.py

from collections import deque
import queue;

def bfs(graph, start, visited):
    #visited check
    visited[start] = True;

    queue = deque([start]);

    #until queue is empty
    while queue:
        node = queue.popleft();
        print(node, end = " " );

        for i in graph[node]:
            if not visited[i]:
                queue.append(i);
                visited[i] = True;

graph = [
    [],#index 0
    [2, 3, 8],#1
    [1, 7],#2
    [1, 4, 5],#3
    [3, 5],#4
    [3, 4],#5
    [7],#6
    [2, 6, 8],#7
    [1, 7]#8
];

# print(graph);

visited = [False] * 9;

bfs(graph, 1, visited);
