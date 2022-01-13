# greedy02_2
import time;

startTime = time.time();
n, k = map(int, input().split());
resultCount = 0;

while True:
    target = (n // k) * k;
    resultCount += (n - target);
    # print("- n :", n,",target: ", target,", resultCount: ", resultCount);
    n = target;

    if n < k:
        break;
    resultCount += 1;
    n //= k;   
    # print("/ N :", n,",target: ", target,", resultCount: ", resultCount);

resultCount += ( n - 1);     
# print("N :", n,",target: ", target,", resultCount: ", resultCount);

endTime = time.time();
print("Total Time: ", endTime - startTime);
