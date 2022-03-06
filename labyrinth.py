# labyrinth
# BFS
# 0 is monster
# 1 is way

from collections import deque

n = 5;
m = 6;

graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
];

#Direction Vector 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        # UP, LEFT, Down, Righ search
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # Out of range ignore
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # Wall ignore
            if graph[nx][ny] == 0:
                continue

            # ! visited
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
   # end node
    return graph[n - 1][m - 1]


print(bfs(0, 0));
# print(bfs(1, 1));
