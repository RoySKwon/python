# set
setDataA = set([1, 1, 2, 3, 4, 4, 5]);
print(setDataA);

setDataB = {2, 3, 6, 6, 7, 8, 9, 9, 10}
print(setDataB);

# sum of sets
print(setDataA | setDataB);

# intersection
print(setDataA & setDataB);

# difference of sets
print(setDataA - setDataB);

#.add()
setDataA.add(23);
print(setDataA);

setDataB.add(0);
print(setDataB)

#.update([ , ])
setDataA.update([20, 88, 77]);
print(setDataA);

#.remove()
setDataB.remove(0);
print(setDataB);

