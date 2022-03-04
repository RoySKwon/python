# GreatestCommonDivisor.py

def gcd(a, b):
	if a % b == 0:
		print("a: ", a,",", "b: ",b);
		return b;
	else: 
		print("a: ", a,",", "b: ",b,",", "a % b: ", a%b);
		return gcd(b, a %b )

print(gcd(192, 162));
# print(gcd(100, 25));
