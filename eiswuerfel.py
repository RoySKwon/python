# eiswuerfel
# DFS  recursive function
# 0 is ice
# 1 is wall


def dfs(x, y):
    #Boundary Over
    if x <= -1 or x >= nRow or y <= -1 or y >= mColumn: 
        return False;
        # print("(" , x,",",y,')', graph[x][y]);

    if graph[x][y] == 0:
        
        # check visited
        graph[x][y] = 1; 

        #Recursive function
        dfs(x - 1, y); # UP
        dfs(x, y - 1); # LEFT
        dfs(x + 1, y); # DOWN
        dfs(x, y + 1); #RIGHT    
        return True;
    return False;

# print(" input Row , Column");

print("Please Row and Column: ");
nRow, mColumn = (map(int, input().split()));
print("n: ", nRow,",","m: ", mColumn);
print("please Graph");
graph = [];
for i in range(nRow):
    graph.append(list(map(int,input())));
print(graph);  

eiswurfel = 0;
for i in range(nRow):
    for j in range(mColumn):
        if dfs(i, j) == True:
            eiswurfel += 1;
            # print(i, j);
            
print("eiswurfel:", eiswurfel);
