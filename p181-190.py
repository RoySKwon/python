# p181-190
""" 
aptMantion = [ ["101", "102"], ["201, 202"], ["302", "303"]];
print(aptMantion);
 """

# price = [[100, 80], [200, 210], [300, 330]];
""" 
price = [["Start", 100, 200, 300], ["End", 80, 210, 330]];
print(price);
print(price[0]);
print(price[1]);
print(price[0][-1]);
print(price[1][-1]);
 """

""" 
stock = {"start":[100, 200, 300], "end" : [80, 210, 330] };
print(stock);
 """

""" 
stock2 = {"10/10":[80, 110, 70, 90], "10/11":[210, 230, 190, 200]};
print(stock2);
 """

from abc import abstractproperty


apart = [[101, 102],[201, 202],[301, 302]];
print(apart);

for row in apart:
    for num in row:
        print(num,"Room");

print("//////////////");

for row in apart[::-1]:
    for num in row:
        print(num,"Room");

print("//////////////");

for row in apart[::-1]:
    for num in row[::-1]:
        print(num, "Room");

print("//////////////");

for row in apart:
    for num in row:
        print(num, "Room");
        # print("-------------");
        print("-" * 5);

print("//////////////");

for row in apart:
    for num in row:
        print(num);
    print("-" * 5);

print("//////////////");

for row in apart:
    for num in row:
        print(num);
print("-" * 5 );