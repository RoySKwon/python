#231-240

def n_plus_1 (n) : #3
    result = n + 1; #4
    print(result);
    return result;

n_plus_1(3);
# print(result);

def make_url(address):
    url_address = "www." + address + ".com"; 
    # print(url_address);
    return url_address;

url = make_url("naver");
print(url);
print(make_url("daum"));

def make_list2(index):
    empty_list = [];
    for x in index:
        empty_list.append(x);
    print(empty_list);   
    return empty_list;

make_list2("fedcba");

def make_list(index):
    print(list(index));
make_list("abcdef");

def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item);
    print(result);        
    return result;

pickup_even([3, 4, 5, 6, 7, 8]);


def convert_int(items):
    # int(string.replace(',', ''))
    int(items.replace(',', '_'));
    print(items);

#replace(',', '')
def convert_int (string) :
    # return (string.replace(',', '.'))
    return int(string.replace(',', ''))

x = convert_int("1,234,567");
print(x)

def Func(num) :
    return num + 4;

a = Func(10);
b = Func(a);
c = Func(b);
print(c);

def Func(num) :
    return num + 4

c = Func(Func(Func(10)))
print(c);

def Func1(num) :
    return num + 4

def Func2(num) :
    return num * 10

a = Func1(10)
c = Func2(a)
print(c)

def Func1(num) :
    return num + 4

def Func2(num) :
    num = num + 2
    return Func1(num)

c = Func2(10)
print(c)

