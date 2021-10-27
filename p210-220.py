# 210-220

""" 
def func(x):
    print(x);

func("Hello");
func("HI");
 """
""" 
def func2(a, b):
    print( a + b);

func2(3, 4);
func2(7, 8);
# func2();
func2("Ho", "Wo");
func2(7, 3);
 """

""" 
def print_with_smile(x):
    print(x + ":D");

print_with_smile("Hello");
 """

def print_upper_price(price):
    print(price * 1.3);

print_upper_price(100);


def print_arithmetic_operation(x, y):
    print(x,"+",y,"=",x + y);
    print(x,"-",y,"=",x - y);
    print(x,"*",y,"=",x * y);
    print(x,"/",y,"=",x / y); # WHY 0

print_arithmetic_operation(3, 4);    

def print_max(x, y, z):
    max_value = 0;
    if x > max_value:
        max_value = x;
    if y > max_value: #WHY elif
        max_value = y;
    if z > max_value:
        max_value = z;
    print(max_value);

print_max(2, 8, 3);