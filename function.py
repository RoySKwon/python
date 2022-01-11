# function

def addReturn(a, b):
    return a + b;

print(addReturn(10, 20));

def addNoReturn(a, b):
    print( a + b );

addNoReturn(100, 70);
addNoReturn(a = 200, b = 33);

#2:03:26
# global

a = 0;
array = [1, 2, 3, 4, 5];

def func():
    global a ;
    print("inFunc",a);
    a += 1;

for i in range(10):
    func();


print("total a", a);

print(array);

def func2():
    # array.append(7);
    global array;
    array.append(7);
    print(array);

func2();

def operator(a, b):
    addVar = a + b;
    subtractVar = a - b;
    multiplyVar = a * b;
    divideVar = a / b;
    return addVar, subtractVar, multiplyVar, divideVar;

a, b, c, d = operator(8, 2);
print(a, b, c, d)

def addFunc(a, b):
    return a + b;

print(addFunc(9, 1));

# Lambda
print((lambda a, b: a+b)(3, 7));
f = (lambda c, d: c * d)(2, 4);
print(f);

# Lambda in sort
array = [("kim", 35), ("Lee", 30), ("Park", 20)];

print(array);

# with function
def my_key(x):
    return x[1];

print(sorted(array, key= my_key));

# no function, with Lambda 
print(sorted(array, key = lambda x: x[1]));

listA = [1, 2, 3, 4, 5];
listB = [6, 7, 8, 9, 10];

result = map(lambda a, b: a + b, listA, listB);
print(result);
print(list(result));
