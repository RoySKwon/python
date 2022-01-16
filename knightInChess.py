# knightInChess

""" 
#int(ord())
value = 'a';
print(type(value),value);
valueOrd= int(ord(value));
print(type(valueOrd),valueOrd);
 """


print("Please Position: ");
knightPosition = input(); # a1
print("Position", type(knightPosition), knightPosition);

rowPosition = int(knightPosition[1]);
print("row:", type(rowPosition),rowPosition);

# columnPosition = int(knightPosition[0]);
columnPosition = int(ord(knightPosition[0])) - int(ord('a')) + 1;
print("column", type(columnPosition),columnPosition);

knightSteps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)];
print(type(knightSteps), knightSteps);

""" 
for position in knightSteps:
    print(position);

 """
theNumberOfCase = 0;

""" 
knightSteps(x, y)
knightSteps(column, row)
knightSteps[0]; //column
knightSteps[1]; //row
 """

for step in knightSteps:
    nextRow = rowPosition + step[0]; #WHY? [0] column
    nextColumn = columnPosition + step[1]; #WHY? [1] row
    print("next:(",nextColumn,",", nextRow, ")");
    
    if nextRow >= 1 and nextRow <= 8 and nextColumn >= 1 and nextColumn <= 8:
        theNumberOfCase += 1;
        print("next:(",nextColumn,",", nextRow, ")", "count:", theNumberOfCase);

print(theNumberOfCase);
