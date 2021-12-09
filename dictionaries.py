# dictionaries

dicData = dict();

dicData['Red'] = 'Apple'
dicData['Yello'] = 'Banana'
dicData['White'] = 'Coconut'

print(dicData);

#key  check
if 'Red' in dicData:
    print("Have a Apple Data");

#key check
if 'Yello' in dicData:
    print("Have a Yello Data");

#value 
# if 'Cocunut' in dicData:
#     print("Have a Green Cocunut");       

print(dicData.keys());
print(dicData.values())

for key in dicData.keys():
    print(dicData[key]);

a = dict();
a['Tom'] = 188;
a['Jack'] = 190;
print(type(a), a);
print(a['Tom']);

b = {
    'Nick': 178,
    'Chris': 180
}
print(type(b), b);
print(b['Chris']);

key_list1 = b.keys();
print(type(key_list1), key_list1);

c = {
    'Tom': 90,
    'Jack': 100
}
print(type(c), c);
# key_list2 = c.keys();
key_list2 = list(c.keys());
print(type(key_list2),key_list2);
