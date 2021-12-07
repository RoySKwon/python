# codeupBasicPy100_calcu

# calculation
""" 
# +, -, %, /
a = int(10);
b = int(2);
print ("%d %d %d %d" %(a+b, a-b, a%b, a/b))

#float /
c = int(5);
d = int (3);
print(5/3);

# 2**
print(2**10)

# ==, !=
a = int(1)
b = int(2)
print(a == b)
print(a != b);

# AND &
# OR |
# XOR ^
# NOT ~

right = int(1);
left = int(0);
print(right,left);

print( right & left );#0
print( right | left );#1
print( right ^ left );#1
print( ~right );# WHY?-2
print( ~left );# WHY? -1
 """

seasion = input();
print({
    "1" : "Winter",
    "2" : "Winter",
    "3" : "Spring",
    "4" : "Spring",
    "5" : "Spring",
    "6" : "Summer",
    "7" : "Summer",
    "8" : "Summer",
    "9" : "Fall",
    "10" : "Fall",
    "11" : "Fall",
    "12" : "Winter",
}.get(seasion));

# print(type(seasion),seasion);
