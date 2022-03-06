# recursive_function.py


def recursive_function():
	print("Call Recursive Function");
	recursive_function(); # ERROR : maximum recursion depth exceeded 
	return 0;

recursive_function();
