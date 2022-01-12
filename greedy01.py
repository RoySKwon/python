# greedy01

# money
money = 1260;
count = 0;

coinsArray = [ 500, 100, 50, 10]; #list
print(coinsArray);

for coin in coinsArray:
    print("coin :", coin);
    print("count :", count);
    count += money // coin; # coin count
    print("count : ", count);

    money %= coin; # remaining meney
    print("money :", money);
    print("------");

print("coins : ", count);
