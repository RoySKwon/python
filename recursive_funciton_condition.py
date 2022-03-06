# recursive_function_condition.py

def recursive_function(i):
	print("Recursive Function: ", i);

	if i == 100:
		return ;
	recursive_function( i + 1);
	print("close :", i, "Recursive Function");

recursive_function(1);
