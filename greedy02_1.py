# greedy02_1

import time;

startTime = time.time();
# print("Start Time : ", startTime);

n, k = map(int, input().split())
# print("n :", n, ", k :", k);
resultCount = 0;

while n >= k:
    while n % k != 0:
        n -=  1;
        resultCount += 1;
        # print("- n: ", n, ", resultCount: ", resultCount);
    n //= k;
    resultCount += 1;     
    # print("/ N: ", n, ", resultCount: ", resultCount);

# print("Total Count :", resultCount);


while n > 1:
    n -= 1;
    resultCount += 1;
print(n, resultCount);

endTime = time.time();
print("End Time   : ", endTime);
print("Total Time : ", endTime - startTime);
