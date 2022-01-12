# greedy02

# 1. 나누기
# 2. 빼기

n, k = map(int, input().split()); # input split space
print("n :", n, ", k:", k);

result = 0;

# 반복문 연산 안에서 n 값이 줄어든다. 복잡도 log 까지 낮춰서 빠르게 동작
while True:
    target =  ( n // k ) * k; # 가장 가까운 k로 나누어 떨어지는 수, 기법
     
    result += ( n - target); # 1 빼는 연산이 몇번 가능한지
    n = target ;
#WHY? 중간에 - 연산 result 빠진다.
    print("resultA: ", result, ", n: ", n, ", k: ", k);

    if n < k:
        break;

    result += 1; # 단계 추가
    n //= k; # 나누어 지는 연산

    print("resultB: ", result, ", n: ", n, ", k: ", k);
    print("-------------")
    
result += (n-1); # 1 빼기 연사
print("result :", result);


