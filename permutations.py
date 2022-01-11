# permutations

from itertools import permutations;

data = ['A', 'B', 'C'];

result = list(permutations(data, 3));
print(result);

""" 
result2 = list(permutations(data, 2));
print(result2);

result3 = list(permutations(data, 1));
print(result3);

result4 = list(permutations(data, 4));
print(result4);
 """