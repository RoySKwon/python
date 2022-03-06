# factorial_iterative.py

# n! = n * (n -1)

def factorial_iterative(n):
	print(n);
	result = 1; # 0! = 1! = 1

	for i in range(result, n+1):
		result = result * i;
		print("result : ",result);
	
	return result;

print(factorial_iterative(5));
