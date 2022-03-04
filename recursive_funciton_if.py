# recursive_function_if.py

def recursive_function(i):
	print("Recursive Function: ", i);	
	if i < 100:
		# return
		print("Calld : ", i+1, "Recursive Function");
		recursive_function(i+1);
		print("close :", i, "Recursive Function");

recursive_function(1);
