# codeupBasicPy100_output

# output

PI = 3.14159265358979;
print(PI);
print("%.2f" %PI);

hour = 5;
minute = 7
second = 3;
print("%d" %second)
print("%2d" %second)
print("%4d" %second)
print("%2d:%2d:%2d" %(hour, minute, second));

#Uni-code
print("\u250C \u252C \u2510");

a = [1,2,3,4];
for i in a:
    print(i, end=" ")
print()

b = [[1,2,3,4,5],[6,7,8,9,0]]
for i in b:
    for j in i:
        print(j, end=" ")
    print();
