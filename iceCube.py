# iceCube.py

#DFS
# 0 is ice space
# 1 is wall space

def dfs(x, y):
	#Out of range
	if x <= -1 or x >= nRow or y <= -1 or y >= mColumn:
		return False;

	# !visited & ice(0)
	if graph[x][y] == 0: 

		#visited check
		graph[x][y] = 1;

		# Recursive Funciton
		dfs(x - 1, y);	#UP
		dfs(x, y - 1);	#LEFT
		dfs(x + 1, y);	#DOWN
		dfs(x, y + 1);	#RIGHT
		return True;
	return False;

#input graph
print("input Row and Column");
nRow, mColumn = map(int, input().split());

# print("input Graph");

graph = [];
for i in range(nRow):
	graph.append(list(map(int, input()))); #push to Stack 
# print(graph);

""" 
nRow = 15;
mColumn = 14;

graph =[
	[0,0,0,0,0,1,1,1,1,0,0,0,0,0],
	[1,1,1,1,1,1,1,0,1,1,1,1,1,0],
	[1,1,0,1,1,1,0,1,1,0,1,1,1,0],
	[1,1,0,1,1,1,0,1,1,0,0,0,0,0],
	[1,1,0,1,1,1,1,1,1,1,1,1,1,1],
	[1,1,0,1,1,1,1,1,1,1,1,1,0,0],
	[1,1,0,0,0,0,0,0,0,1,1,1,1,1],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,1,1,1,1,1],
	[0,1,1,1,1,1,1,1,1,1,1,0,0,0],
	[0,0,0,1,1,1,1,1,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,1,1,1,1,0,0,0],
	[1,1,1,1,1,1,1,1,1,1,0,0,1,1],
	[1,1,1,0,0,0,1,1,1,1,1,1,1,1],
	[1,1,1,0,0,0,1,1,1,1,1,1,1,1]
];
 """

# Count True
result = 0;
for i in range(nRow):
	for j in range(mColumn):
		# Fist visited
		if dfs(i, j) == True:
			result = result +1;

print(result);
