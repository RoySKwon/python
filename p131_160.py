#131_140
#141_150
#151_160

#iterate

""" 
fruit = ["Apple", "Banana", "Orange"];

for x in fruit:
    print(x);
 """

# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
""" 
for varTxt in ["A", "B", "C"]:
    print("Change", varTxt);

for varTxt in ["A", "B", "C"]:
    tmpTxt = varTxt.lower();
    print("Change", tmpTxt);

for varStr in ['10', '20', '30']:
    print(type(varStr),varStr);

for varInt in [10, 20, 30]:
    print(type(varInt),varInt);

for varChr in [1, 2, 3, 4]:
    # print("-------");
    print(type(varChr), varChr);
 """


""" 
Cost = [100, 200, 300];
print(Cost);

Tex = 10;
for productCost in Cost:
    productCost = productCost + Tex;
    print(productCost);
 """

""" 
menuLists = ["PASTA", "PIZZA", "KIMCHI"];

for todaysMenu in menuLists:
    print("Today's Menu : ",todaysMenu);
 """

#len
""" 
telecomCompany = ["SKTelecom", "LGTelecom", "KTF"];

for stringCount in telecomCompany:
    print(len(stringCount));

 """
""" 
homeAnimal = ["Dog", "Cat", "Pig"];
for animal in homeAnimal:
    print(animal, len(homeAnimal));
    # print(animal[:1:]);
    print(animal[0]);
 """

#" ".format(,)
""" 
ninetonine = [1, 2, 3, 4, 5, 6, 7, 8, 9 ];

for x in ninetonine:
    # print("3 x ", x, "=", 3 * x  );
    print("3 x {} = {}".format(x, 3 * x));
 """ 
""" 
alphabet = ["A", "B", "C", "D", "E", "F"];

for spel in alphabet[::2]:
    print(spel); 

for spel in alphabet[::-1]:
    print(spel);
 """
""" 
mixNumber = [3, -20, -3, 44]

for negativNumber in mixNumber:
    if(negativNumber < 0):
        print(negativNumber);

 """


""" 
rowList = [3, 100, 23,44, 72];

for multiple3 in rowList:
    if multiple3 %3 == 0: 
        print(multiple3)
 """


"""  
less20multiple3number = [13, 21, 12, 14, 30, 18];

for number in less20multiple3number:
    if( number < 20 ) and ( number %3 == 0 ):
        print(number);
 """

""" 
sentenceList = ["Iam", "study", "python", "language", "!"];
for sentenceWord in sentenceList:
    if( len(sentenceWord) > 3 ):
        print(sentenceWord);
    # print(len(sentenceWord), sentenceWord);
 """

#.isupper()
""" 
alphabetList = ["A", "b", "c", "D", "E", "f"];

for bigAlpha in alphabetList:
    if(bigAlpha.isupper()):
        print( bigAlpha); 
 """

#.islower()
""" 
for bigAlpha in alphabetList:
    if(bigAlpha.islower()):
        print(bigAlpha);
 """

""" 
animalsList = ['dog', 'cat', 'pig'];
for animal in animalsList:
        # print(animal[:1:].upper() + animal[1:]);
        print(animal[0].upper() + animal[1:]);
 """

""" 
filesList = ['hello.py', 'world.c', 'programm.cpp'];

for fileName in filesList:
    print(fileName.split('.')[0]);
 """

""" 
filesList = ['hello.py', 'world.c', 'programm.cpp', 'Games.h'];
for headerFile in filesList:
    if(headerFile.split('.')[1] == "h"):
        print(headerFile);
 """

""" 
filesList = ['hello.py', 'world.c', 'programm.cpp', 'Games.h'];
for headerFile in filesList:

    if(headerFile[-1] == 'h'):
        print(headerFile);
 """

 #160

programList = ['std.h', 'main.c', 'define.h', 'batch.py'];

for program in programList:
    if(program[-1] == 'h') or (program[-1] == 'c'):
        print(program);


