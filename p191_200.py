#191-200

#  OHLC (open/high/low/close)

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# print(data);
# 0.014 %

""" 
for line in data:
    # print("-" * 30);
    for column in line:
        print(column, column * 0.00014, column * 1.00014);
    print("-" * 30);
 """

# 1 Demension List
""" 
pricePlusFee = [];

for line in data:
    for column in line:
        pricePlusFee.append(column * 1.00014);
print(pricePlusFee);
 """

# 2 Demension List
""" 
sub1Demen = [];
sub2Demen = [];

for line in data:
    for column in line:
        sub1Demen.append(column * 1.00014);
    sub2Demen.append(sub1Demen);    
print(sub1Demen);   
print("*" * 30);         
print(sub2Demen);            
 """

#195
ohlc = [
        ["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]
        ]
# print(ohlc);

""" 
for row in ohlc:
    print(row[3]);
 """

for row in ohlc[1:]:
    print(row[3]);