# libs

# sum()
from types import MappingProxyType


sumResult = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
print(sumResult);

# min()
minResult = min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
print(minResult);

# max()
maxResult = max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
print(maxResult);

# eval()
evalResult = eval("(3+2)*5");
print(evalResult);

# sorted()
sortResult = sorted([ 10, 2, 7, 3, 4]);
print(sortResult);

reverseResult = sorted([ 10, 2, 7, 3, 4], reverse=True );
print(reverseResult);

array = [("kim", 35), ("Lee", 20), ("Park", 30)];
reverseLambda = sorted(array, key = lambda x: x[1], reverse=True);
print(reverseLambda);