# 081_100 
# dictionary
# {key: value}

# Tuple
from types import prepare_class


a, b, *c = (0, 1, 2, 3, 4, 5)
print(a);
print(b);
print(c);


#list
#left , _
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(scores);
*validLeftScores, _, _ = scores;
print(validLeftScores);
*validLeftScores,_ = scores;
print(validLeftScores);
*validLeftScores, = scores;
print(validLeftScores);

# list
#right
oneTemp, twoTemp, *validRightScores = scores;
print(validRightScores);
print(oneTemp);
print(twoTemp);

# list
#center
leftTemp, *validCenterScores, rightTemp = scores;
print(type(leftTemp)); 
print(leftTemp); 

print(type(validCenterScores)); 
print(validCenterScores); 

print(type(rightTemp));
print(rightTemp);

emptyDic = [];
print(type(emptyDic));
print(emptyDic);

emptyDic = ();
print(type(emptyDic));
print(emptyDic);

#dictionary
emptyDict = {};
print(type(emptyDict));
print(emptyDict);

autoCost = { "Audi" : 50000, "BMW" : 60000, "Mercedes-Benz" : 70000, "VolksWagen" : 40000};
print(autoCost);
autoCost["HYUNDAI"] = 30000;
print(autoCost);
print("Audi Cost : ",autoCost["Audi"] );
autoCost["Audi"] = 55000;
print("New Audi Cost : ",autoCost["Audi"] );
del autoCost["VolksWagen"];
print(autoCost);
print(autoCost["HYUNDAI"]);
# print(autoCost["TOYOTA"]);

# autoInventory = { "Audi" : 50000 : 100, "BMW" : 60000 : 50 , "VolksWagen" : 40000 : 300};
autoInventory = { "Audi" : [50000, 100], "BMW" : [60000, 50] , "VolksWagen" : [40000, 300]};
print(autoInventory);

print("BMW Price : ", autoInventory["BMW"][0], ", Inventroy : ", autoInventory["BMW"][1]);
autoInventory["Porsche"] = 9000 ;
print(autoInventory);
autoInventory["Porsche"] = [9000, 10] ;
print(autoInventory);

#dictionary to list
autoInventory = { "Audi" : 50000, "BMW" : 60000, "VolksWagen" : 40000};
print(autoInventory);
print(type(autoInventory));
autoInventoryList = list(autoInventory);
print(autoInventoryList);
print(type(autoInventoryList));

#dictionary to list with keys
autoInventory = { "Audi" : 50000, "BMW" : 60000, "VolksWagen" : 40000};
autoInventoryKey = autoInventory.keys();
print(type(autoInventoryKey));
print(autoInventoryKey);
autoInventory = list(autoInventoryKey);
print(type(autoInventory));
print(autoInventory);

#dictionary to list with keys method in list()
autoInventory = { "Audi" : 50000, "BMW" : 60000, "VolksWagen" : 40000};
autoInventoryListWithKey = list(autoInventory.keys());
print(type(autoInventoryListWithKey));
print(autoInventoryListWithKey);

#dictionary to list with values method in list()
autoInventory = { "Audi" : 50000, "BMW" : 60000, "VolksWagen" : 40000};
autoInventoryListWithValues = list(autoInventory.values());
print(type(autoInventoryListWithValues));
print(autoInventoryListWithValues);
print(autoInventory);

autoInventory = { "Audi" : 50000, "BMW" : 60000, "VolksWagen" : 40000};
addModels = {"Porsche": 80000, "HONDA": 35000};
print(type(addModels));
print(addModels);
autoInventory.update(addModels);
print(autoInventory);


#combine dictionary wit zip()
keys = ("apple", "pear", "peach");
vals = (300, 250, 400);

#new init dictionary 
combineDict = dict(zip(keys,vals));
print(type(combineDict));
print(combineDict);

# two list to one dictionary with zip() method in dict()
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
print(type(date), type(close_price));

close_data = dict(zip(date,close_price));
print(type(close_data));
print(close_data);