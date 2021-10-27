# 201_210


def print_coin():
    print("Bit Coin");

MAX_NUM = 100;
for index in range(MAX_NUM):
# for index in MAX_NUM: # error 'int' object is not iterable
    print_coin();


def message1():
    print('A');

def message2():
    print('B');

def message3():
    for i in range(3):
        message2();
        print("C");
    message1();

message3();
