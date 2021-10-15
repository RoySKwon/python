# 071_080 Tuples
# 파이썬 튜플은 순서가 있지만 
# 수정 불가능한 자료구조

tuplesVariable = ();
print(type(tuplesVariable));

tupleMovies = ("IronMan", "SuperMan", "BatMan");
print(type(tupleMovies));
print(tupleMovies);
print(tupleMovies[0]);
print(tupleMovies[2]);
print(tupleMovies[-1:]);
print(tupleMovies[::-1]);

t = (1, 2, 3)
# t[0] = 'a' // don't change the element in Tuple
print(t);

# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# (1) // int
numTuple1 = (1);
print(type(numTuple1));

# (1,)// tuple
numTuple2 = (1,);
print(type(numTuple2));

# no parenthesis is Tuple
isTuple = 1,2,3,4 ;
print(type(isTuple));

# smallChar = (a, b, c);
smallCharList = ['a', 'b', 'c'];
smallCharTuple = ('a', 'b', 'c');
print(type(smallCharList));
print(type(smallCharTuple));

smallCharList[0]  = 'A';
print(smallCharList);

# smallCharTuple[1] = 'B'; // Tuple don't support item assignment

smallCharTuple = ('a', 'B', 'c');
print(smallCharTuple);

tupleString = ("SAMSUNG", "LG", "HYUNDAI");
print(tupleString);
print(type(tupleString)); 
tupleToList = list(tupleString);
print(type(tupleToList));
print(tupleToList);

tempTuple = ('apple', 'banana', 'cake')
aElement, bElement, cElement = tempTuple
print(aElement, bElement, cElement)
print(type(tempTuple));
print(type(aElement));
print(aElement);
print(type(bElement));
print(bElement);
print(type(cElement));
print(cElement);

# range type
for i in range(1, 100):
    print(i,end = ',');

#range(start, stop, sep)
oneToHundred = range(1, 100);
print(type(oneToHundred));
print(oneToHundred);    

range
evenNumber = range(2, 100, 2);
print(tuple(evenNumber));

# not enough values to unpack
# star expression
lessTuple = ("Amazon","Facebook");
aElement, bElement, *cElement = lessTuple;
# *aElement, bElement, cElement = lessTuple;
print(aElement, bElement, cElement);
print(aElement);
print(bElement);
print(cElement);

print(type(aElement));
print(aElement);

# too many values to unpack
# star expression
lessTuple = ("Amazon","Facebook","Apple","Goolge","Micro Soft");
*aElement, bElement, cElement = lessTuple;
print(aElement, bElement, cElement);
print(aElement);
print(bElement);
print(cElement);
