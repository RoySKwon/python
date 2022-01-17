# recursiv03
# Factorial with recursive
# Test Iterative Vs Recursive
# Recursive fast

import time

startTime = time.time();

# number = int(input());
number = 100;

#iterative

def factorial(number):
    result = 1;
    for i in range(1, number + 1):
        result *= i;
    return result;

print("result: " ,factorial(number));


#recursive
"""  
def factorialRecursive(number):
    if number < 1:
        return 1;
    return number * factorialRecursive(number - 1 );

print("result : ",factorialRecursive(number));
 """
endTime = time.time();
print("Total Time: ", endTime - startTime);
