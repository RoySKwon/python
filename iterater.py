# iterater

i = 1;
result = 0;

while i <= 10:
    if i % 2 == 1:
        result += i;
    i += 1;
    print(result);
print(type(result), result); 

arrayList = [9, 8, 7, 6, 5];

for x in arrayList:
    print(x);

arrayTuple = (1, 2, 3, 4, 5);

for x in  arrayTuple:
    print(x);

result = 0;
for x in range(10):
    result += x;
    print(result);

result = 0;
for x in range(1, 101):    
    result += x;
    print(f"x {x} result {result}" )
print(result);    

result = 0;

for x in range(1, 11):
    if x % 2 == 0:
        print("continue", x);
        continue;
    result += x;
print(result);

i = 1;
while True:
    print(i);
    if i >= 5 :
        break;    
    i += i;
print("exit: ", i)

scores = [ 100, 95, 45, 75, 65, 50, 80, 90, 100, 77];
cheating_student_list = {0, 8}

for x in range(10):
    if x in cheating_student_list:
        continue;
    if scores[x] >= 60:
        print(scores[x], "Success");
    else:
        print(scores[x], "FAIL");    

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, '=', i * j);
    print("");    