# listComprehension

import time;

array = [];
print(array);

# start Time
start_Time1 = time.time();

# list.append()
for x in range(20):
    array.append(x);
print(array);

# end Time
end_Time1 = time.time();
print("append: ", end_Time1 - start_Time1);

# start Time
start_Time2 = time.time();

array = [y for y in range(20)];
print(array);

# end Time
end_Time2 = time.time();
print("comprehension: ",end_Time2 - start_Time2);

if end_Time1 - start_Time1 > end_Time2 - start_Time2:
    print ("Fast comprehension in list ");
else:
    print("Fast append in list");


# 4 x 3


n = 4;
m = 3;

# Good
array = [ [0] * m for _ in range(n)]
print(array);

array[1][1] = 5;
print(array);

# Bad
array = [ [0] * m ] * n;
print(array);

array[1][1] = 5;
print(array);

summary = 0;
for i in range(1, 10):
    summary += i;
print(summary);

for _ in range(10):
    print("Hello");
