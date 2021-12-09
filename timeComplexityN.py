# timeComplexityN
import time

# 1s 500,000,000
# C 1s ~ 3s
# Python 5s ~ 15s
# 1s N = 5,000

# N 500 O(N3)
# N 2,000 O(N2)
# N 100,000 O(NlogN)
# N 10,000,000 O(N) 

# start_time = time.time();
# end_time = time.time();
# print("time : " , end_time - start_time)

# N = 5 
# O(N)
start_time = time.time();
print(start_time);

arrayX = [3, 5, 1, 2, 4];
summary = 0;

for x in arrayX:
    summary += x;
print(summary);
end_time = time.time();
print("time : " , end_time - start_time)
