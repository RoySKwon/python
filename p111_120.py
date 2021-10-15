# 111_120
# condition

# print(input("Please input : "));

""" 
user = input("input:");
print(user * 2);
 """

#string to int
""" 
inputNumber = input("input Number :");
print(inputNumber);
print(type(inputNumber));

print(int(inputNumber) + 10);
print(type(inputNumber));
 """

# string to int with int() method
""" 
result = input("Input nummber:");
print(result);
if (int(result) % 2 == 0):
    print("even number");
else :
    print("odd number");    
 """    

""" 
inputNumber = input("Please input : ");
print(inputNumber);
resultNumber = int(inputNumber) + 20;

if int(resultNumber) >= 255:
    print(255);
else:
    print(resultNumber);    
 """

""" 
inputNumber = input("Please input : ");
print(inputNumber);
resultNumber = int(inputNumber) - 20;
print(resultNumber);

if resultNumber < 0 :
    print(0)
elif resultNumber > 255:
     print(255);
else:
    print(resultNumber);
 """

""" 
time = input("What time is it now ?");
print(time);
print(time[0:]);
print(time[:2:]);
print(time[-2:]);

if(time[-2:] == "00"):
    print("Exactly time : ", time[:2:]);
else:
    print("no Excatly time");    
 """
# 117
""" 
fluit = ["apple", "banana", "orange"];
myFruit= input("input fruit :");
print(myFruit);

if myFruit in fluit:
    print(" Good");
else:
    print("We don't have : ",myFruit);
 """

""" 
if(myFruit ==fluit[0]):
    print("You choice : ", fluit[0]);
elif(myFruit == fluit[1]):
    print("You choice : ", fluit[1]);
elif(myFruit == fluit[2]):
    print("You choice : ", fluit[2]);
 """
""" 
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"];
print(warn_investment_list);
myChoiceCompany = input("Please Choce investmet company: ");
print(myChoiceCompany);

if(myChoiceCompany in warn_investment_list):
    print("warning !!!");
else:
    print("Good Luck !");    
 """

# key

seasonFruit = {"spring" : "strawberry", "summer" : "watermelon", "fall" : "apple", "winter" :  "nix" };
print(seasonFruit);
mySeason = input("Please choice Season : ");

print(mySeason);
if(mySeason in seasonFruit):
    print("Good Choice Season");
else:
    print("So so ");     

#velue
if(mySeason in seasonFruit.values()):
    print("Nice fruit");
else:
    print("not bad");    
