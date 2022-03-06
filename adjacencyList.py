# adjacencyList.py

#3row
graph = [[] for _ in range(3)];

print(graph);

#(node, edge distance)
graph[0].append((1, 7));
graph[0].append((2, 5));

graph[1].append((0, 7));

graph[2].append((0, 5));

print(graph);
