# dataType

a = 1e9;
# print(type(a),a,format(a,'b'));

a = int(1e9);
print(type(a),a,format(a,'b'));
# print(type(a),a);


a = 75.25e1;
print(a);

a = 3954e-3;
print(a);

# float 0.9 => Binary
 
a = 0.3 + 0.6
print(type(a), a);

if a == 0.0:
    print(True);
else:
    print(False)    

#round()
a = round(0.3 + 0.6, 4)
print(type(a), a);

if round(a,4) == 0.9:
    print(True);
else:
    print(False)    

a = 7;
b = 3;

print( a / b );
print( a % b );
print( a // b );
print( a ** b );
print( a ** 0.5 );
