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

#224
