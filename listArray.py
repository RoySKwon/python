# listArray

a = [];
print(type(a),a);

a = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print(type(a),a);
print(a[4]);
a[8] = 0;
print(a);

b = [0];
print(b);

n = 10;
c = [0] * 10;
print(c);

# indexing
print(a[2]);

# slicing
print(a[4:7])

# list comprehension
array1 = [i for i in range(10)];
print(array1);

array2 = [ j for j in range(50)];
print(array2);

# list comprehension with condition
array3 = [ x for x in range(20) if x % 2 == 1 ];
print(array3);

array4 = [ y for y in range(20) if y %2 == 0];
print(array4);

array5 = [z * z for z in range(1, 10)];
print(array5);