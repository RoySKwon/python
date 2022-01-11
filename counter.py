# counter

from collections import Counter;

colorCounter = Counter(['red', 'blue', 'green', 'red', 'green', 'blue', 'blue', 'green', 'green']);

print(colorCounter);
print("blue: ", colorCounter['blue']);
print("red: ", colorCounter['red']);
print("green: ", colorCounter['green']);
print("yello: ", colorCounter['yello']);
print(dict(colorCounter));
