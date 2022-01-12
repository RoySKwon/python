# greedy03

data = input();
print(type(data), data);

result = int(data[0]);
print(type(result), result);

for i in range(1, len(data)):
    num = int(data[i]);
    print("num :", num);
    if( num <= 1 or result <= 1):
        result += num;
        print("result +: ", result);
    else:
        result *= num;
        print("result *:", result);
    print("-------");
print(result);