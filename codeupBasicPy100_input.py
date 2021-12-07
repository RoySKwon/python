# codeupBasicPy100_input

# input

temp = input();
print(temp);
print(type(temp ));
tempInt = int(temp);
print(type(tempInt),tempInt);
tempFloat = float(temp);
print(type(tempFloat),tempFloat);

# two number input
a,b = map(int, input().split());
# a,b = map(int, input().split(","));
print(a);
print(b);

#two string input
c, d = map(str, input().split());
print(c);
print(d);

# one line numbers to list
f = list( map(int, input().split()));
print(type(f),f);

# 2G Array
g = [list( map(int, input().split()))
    for _ in range(2)]  #//WHY? range(10) row10
print(g);
