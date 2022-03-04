# factorial_recursive.py

# n! = n * (n -1)

def factorial_recursive(n):
	print("n : ", n);
	if n <= 1:
		# 0! = 1, 1! = 1;
		print("return :", n);
		return 1;
	return n * factorial_recursive(n-1);

print(factorial_recursive(5));
