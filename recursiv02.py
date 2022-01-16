# recursiv02
#Factorial with iterative
import time;

""" 
print("Input Number");
number = int(input());
print(number);
 """
startTime = time.time();

def factorialIterative(number):
    result = 1;

    for i in range(1, number + 1):
        result *= i;
        # print("result",result);
    
    return result;

endTime = time.time();
# print("Factorial with Iterative :", factorialIterative(number));
print("Factorial with Iterative :", factorialIterative(1000));
print("Total Time:", endTime - startTime);