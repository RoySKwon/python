#171-180


""" 
price_list = [32100, 32150, 32000, 32500];

for price in price_list:
    print(price);
 
for price in range(4):
    print(price_list[price]);
 
for price in range(len(price_list)):
    print(price_list[price]);

for price in range(len(price_list)):
    print(price, price_list[price]);


for price in range(len(price_list)):
    print( (len(price_list) -1) - price, price_list[price]);

for price in range(1, len(price_list)):
    print(  90 + (10 * price), price_list[price]);
 """

# 0, 1, 2, 3
# 0,1
# 1,2
# 2,3

# alphabetList = ['A', 'B', 'C', 'D'];

# for abc in alphabetList:
#     if(abc %2 == 0):
#         print("/n");
#     print(abc);

# print(alphabetList[0], alphabetList[1]);
# print(alphabetList[1], alphabetList[2]);
# print(alphabetList[2], alphabetList[3]);

# for i in [0, 1, 2]:
#     print(alphabetList[i], alphabetList[i+1]);

""" 
for i in range(len(alphabetList) - 1):
    print(alphabetList[i], alphabetList[i+1]);
 """
"""  
for i in range(len(alphabetList)-1, 0, -1):
    print(alphabetList[i], alphabetList[i-1]);
 """

# A, B, C
# B, C, D
# C, D, E
""" 
alphabetList = ['A', 'B', 'C', 'D', 'E'];

print(len(alphabetList));

for x in range(1, 4):
    print(alphabetList[x-1], alphabetList[x], alphabetList[x+1]);

for x in range(1, len(alphabetList)-1):
    print(alphabetList[x-1], alphabetList[x], alphabetList[x+1]);
 """    
""" 
myList = [ 100, 200, 400, 800];

print(myList[1] - myList[0]);
print(myList[2] - myList[1]);
print(myList[3] - myList[2]);

print(len(myList))

for x in range(len(myList)-1):
    print(myList[x+1] - myList[x]);
 """    

""" 
myList = [100, 200, 400, 800, 1000, 1300];
print(len(myList));

for x in range(1, len(myList) -1 ):
    print(myList[x - 1], myList[x], myList[x + 1],"Avl",float(myList[x - 1] + myList[x] + myList[x+1])/3);
    print(myList[x - 1], myList[x], myList[x + 1],"Avl",abs(myList[x - 1] + myList[x] + myList[x+1])/3);
 """
lowPrices  = [100, 200, 400, 800, 1000]
highPrices = [150, 300, 430, 880, 1000]

# .append()

fiveVolatility = [];
print(fiveVolatility);
for x in range(5):
    fiveVolatility.append(highPrices[x] - lowPrices[x]);
print(fiveVolatility);    
for i in range(5):
    print(fiveVolatility[i]);