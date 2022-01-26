# eiswuerfel
# DFS  

def dfs(x, y):
    #Boundary Over
    if x <= -1 or x >= nRow or y <= -1 or y >= mColumn: 
        return False;
    print("(" , x,",",y,')', graph[x][y]);

    if graph[x][y] == 0:
        #check
        graph[x][y] = 1;

        #Recursive function
        dfs(x - 1, y); # UP
        dfs(x, y - 1); # LEFT
        dfs(x + 1, y); # DOWN
        dfs(x, y + 1); #RIGHT    
        return True;

    result = False;

print(" input Row , Column");

#space
nRow, mColumn = (map(int, input().split()));
print(nRow, mColumn);

graph = [];

for i in range(nRow):
    # graph.append(map(int,input()));
    graph.append(list(map(int,input())));

print(type(graph), graph);  

eiswurfel = 0;

for i in range(nRow):
    for j in range(mColumn):
        if dfs(i, j) == True:
            eiswurfel += 1;
            
print(eiswurfel);
