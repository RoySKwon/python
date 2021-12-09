# etcMathod

# list.append() //one element in list O(1)
# list.sort() // ASC O(NlogN)
# list.sort( reverse = True ) // DESC O(NlogN)
# list.reverse() // all  O(N)
# insert(index, value) // O(N)
# list.count(value) // find and count O(N)
# list.remove(value) //one value delete O(N)

listSample = [1, 8, 2];
print("list: ", listSample);

listSample.append(7);
print("appand: ", listSample);

listSample.sort();
print("sort ASC: ", listSample);

listSample.sort(reverse = True);
print("sort DESC: ", listSample);

listSample.reverse();
print(listSample);

listSample.insert(2, 7);
print(listSample);

print("value 7 : ", listSample.count(7));
print("value 8 : ", listSample.count(8));

listSample.remove(8);
print(listSample);

valueAllDelete = [1, 2, 3, 4, 4, 8, 8, 8, 9];
print(valueAllDelete);
print(valueAllDelete.count(8));

remove_set = {4, 8}
result = [ x for x in valueAllDelete if x not in remove_set ]
print(result);