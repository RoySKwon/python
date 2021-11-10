# 221-231

def print_reverse(stringx):
    print(stringx[::-1]);
"""     
    for index in stringx[::-1]:
        print(index);
 """
print_reverse("python");

# list with sum
def print_score(listx):
    print("SUM :",sum(listx));
    print("LEN :", len(listx));
    print(sum(listx)/len(listx));
print_score ([1, 2, 3]);



def print_even(listNums):
    print(listNums);
    for x in listNums:
        print(x);
        if(x % 2 == 0):
            print("if :",x);

        elif(x % 2 != 0):
            print("else if :",x);
        else:
            print("Error");         
print_even ([1, 3, 2, 10, 12, 11, 15]);



def print_keys(dicInfo):
    for index in dicInfo: 
        print(index);

print_keys({"Name":"James", "Age":30, "Sex":0});


my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}


def print_value_by_key(my_dict, key):
    print(my_dict[key]); #WHY [key]
print_value_by_key(my_dict, "10/26");
# print_value_by_key(my_dict, "10/27");



def print_5xn(number):
    chunk_number = int(len(number)/5)
    print(chunk_number);
    print(range(chunk_number));
    for x in range(chunk_number):
        print(number[ x * 5: x * 5 + 5 ]);  #//WHY [ x * 5: x * 5 + 5 ] #226

print_5xn("1234567890");


def print_mxn(line, num):
    chunk_num = int(len(line) / num);
    print(range(chunk_num));
    print(range(chunk_num + 1));
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num]);

print_mxn("1234567890", 3);


def calc_salary(Money):
    monthly_salary = int(Money / 12);
    print(monthly_salary);
    return monthly_salary; #//WHY return value where

calc_salary(12000000);

def my_print (a, b) :
    print("Left Value: ", a);
    print("Right Value: ", b);

my_print(a=100, b=200)


