# codeupBasicPy100_Trans

#format(value ,'x') 
num = int(10);#Decimal
print(type(num),num); 
print('2:',format(num,'b')); #Binary
print('8:',format(num,'o')); #Octal
print('16:',format(num,'x')); #hexadecimal
print('16:',format(num,'X')); #hexadecimal

# Trans to Decimal int(Value, 16) 

# Binary to Decimal
binaryTemp = "1010";
print(type(binaryTemp),binaryTemp);
print(int(binaryTemp)) #Binary
print(int("0b" + binaryTemp, 2));

#Octal to Decimal
octalTemp = "13";
print(type(octalTemp), octalTemp);
print(int(octalTemp));
print(int(octalTemp, 8));
print(int("0o" + octalTemp, 8));

#Hexadecimal
hdTemp = "F";
# print(int(hdTemp));
print(int(hdTemp,16));
print(int("0x" + hdTemp,16));

num ="FF";
print(num);
# print(int(num))
print(int(num,16))
print(format(int(num,16),'o'));