# 001_010 print
# 011_020 veriable

temp = "Hello World";
print(temp);

print("MARVER's COMIC");

print("Herry 'Come on !'' ");
# print('Herry "Come on !" ');

print("Hi Hello ! \n Welcome\t to \t Seoul");

print("Today","Monday");

# print("Kakao; Naver; Samsung; SK");
print("Kakao", "Naver", "Samsung", "SK");
print("Kakao", "Naver", "Samsung", "SK", sep=";");
print("Kakao", "Naver", "Samsung", "SK", sep="/");

# print("first");print("second");
print("first", "second", end="");print("third");

num = 0;
num = 5/3
print(num);
print(round(num));

stocksSamsungPrice = 500000;
stocksSamsung = 10;
totalPrice = stocksSamsung * stocksSamsungPrice
print(totalPrice);

시가총액 = 298000000000000;
현재가 = 500000;
PER = 15.79;

# type()
print("시가총액: ", 시가총액, type(시가총액));
print("현재가: ", 현재가, type(현재가));
print("PER: ", PER, type(PER));

s = "Hello";
t = "Python";
print(s,"!",t);
print(s+t);

num1 = 2 + 2 * 3;
print(num1);

a = 128;
print("a=", a, type(a));

b = 256;
print("b=", b, type(b));

c = 3.14;
print("c=", c, type(c));

# int();
# float();
# str();
# round();

num_sting = "720";
num_int = int(num_sting);
print(num_int, type(num_int));

num_sting2 = "3.14";
# num_int = int(num_sting2); //invalid literal for int()
# num_int = int(round(num_sting2));// Type str doesn't define __round__ method
num_int = float(num_sting2);
print(num_int, type(num_int));

num_int = 100;
print(num_int, type(num_int));

num_string = str(num_int);
print(num_string, type(num_string));

num_string = "3.14";
print(num_string, type(num_string));

num_float = float(num_string);
print(num_float, type(num_float));

string_year = "2020";
print(string_year, type(string_year));
int_year = int(string_year);
print(int_year, type(int_year));
print(int_year - 1);
print(int_year - 2);
print(int_year - 3);

monthPrice = 499.99;
print(monthPrice, type(monthPrice));
totalmonths = 36;
print(totalmonths, type(totalmonths));
totalPrice = totalmonths * monthPrice ;
print(totalPrice, type(totalPrice));
print(round(totalPrice));


