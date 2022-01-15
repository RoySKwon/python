# upDownLeftRight
# Simulation

x, y = 1, 1; # initial
print("Start position:", "(",x,",",y,")");

moveTypes = ['L', 'R', 'U', 'D'];
dx = [0, 0, -1, +1];
dy = [-1, +1, 0, 0];

print("Prease insert Number: "); #5
rowColumn = int(input()); 
print(" Row and Column : ", rowColumn, "x", rowColumn);

print("Prease insert Map:"); # R R R U D D L L L L

directionPlan = input().split();# with space

for plan in directionPlan:
    for i in range(len(moveTypes)):#4
        print("plan:", plan, "moveTypes[i]:", moveTypes[i]);
        if plan == moveTypes[i]:
            nextX = x + dx[i];
            nextY = y + dy[i];
            print("Next:", nextX,",", nextY); 

    if nextX < 1 or nextX > rowColumn or nextY < 1 or nextY > rowColumn : 
        print("! Range over");
        continue; #skip

    x, y = nextX, nextY;

print("Destination:","x", x,",y", y);     
