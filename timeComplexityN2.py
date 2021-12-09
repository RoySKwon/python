# timeComplexityN2
import time

start_time = time.time();
# O(N2)
arrayX = [1, 2, 3, 4, 5];
summary = 0;

for x in arrayX:
    for y in arrayX:
        temp = x * y;
        print(temp);

end_time = time.time();
print("time : " , end_time - start_time)
