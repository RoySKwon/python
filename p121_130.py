#121_130

#upper(), lower(), islower(), upper()

""" 
isChar = input("input char :");
print(isChar);

if(isChar.islower()):
    print("lower");
    print(isChar.upper());
elif(isChar.isupper()):
    print("upper");
    print(isChar.lower());
else:
    print("It is not character");
 """

""" 
grade = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F':6};
print(grade);
print(grade.keys());
print(grade.values());
myScore = input("input score : ");

if ( 81 <= int(myScore) <=100 ): print(" Score is Grade : A " );
elif ( 61 <= int(myScore) <=80 ): print(" Score is Grade : B " );
elif ( 41 <= int(myScore) <=60 ): print(" Score is Grade : C " );
elif ( 21 <= int(myScore) <=40 ): print(" Score is Grade : D " );
elif ( 00 <= int(myScore) <=20 ): print(" Score is Grade : E " );

else : print("Error");
 """

#split()
""" 
print("Exchange to KRW(South Korea) ");
countrysRate = {"USA": 1.182, "EURO": 1.371, "JAPAN": 10.63, "CHINA": 183.45};
print(countrysRate.keys());

choiceCountry = input("input DATA => \"Country and Space and Value \"(ex. GBP  1.601) : ");

rowData = choiceCountry.split(" ");
# print(rowData[0], rowData[1]);
if(rowData[0] == "USA"):
    print("USA USD") 
    exchangeRate = float(rowData[1]);
    print("South Korea :",exchangeRate * 1.182,"KRW");
elif(rowData[0] == "EURO"): 
    print("EURO EUR");
    exchangeRate = float(rowData[1]);
    print("South Korea :", exchangeRate * 1.3715,"KRW");
elif(rowData[0] == "JAPAN"): 
    print("JAPAN JPY");
    exchangeRate = float(rowData[1]);
    print("South Korea :", exchangeRate * 10.635,"KRW");
elif(rowData[0] == "CHINA CNY"): 
    print("CHINA");
    exchangeRate = float(rowData[1]);
    print("South Korea :", exchangeRate * 183.45,"KRW");
else:
    print("Error");
 """
""" 
maxNumber = 0;
print(maxNumber);

tmpNumber1 = input("input number 1 :");
tmpNumber2 = input("input number 2 :");
tmpNumber3 = input("input number 3 :");

if(tmpNumber1 >= tmpNumber2 and tmpNumber1 >= tmpNumber3) :
    maxNumber = tmpNumber1;
    print(maxNumber);
elif(tmpNumber2 >= tmpNumber1 and tmpNumber2 >= tmpNumber3):
    maxNumber = tmpNumber2;
    print(maxNumber);
elif(tmpNumber3 >= tmpNumber1 and tmpNumber3 >= tmpNumber2):
    maxNumber = tmpNumber3;
    print(maxNumber);
else:
    print("Error");
 """    
""" 
telecomNumber = {"SK Telecom": "011", "KT Telecom" : "016", "Shinsegi Telecom" : "017", "HANSOL Telecom" : "018", "LG Telecom": "019", "All": "010"};
print(telecomNumber.keys());
phoneNumber = input("Please insert Phone number (ex. 010-555-5555) : ");
print(phoneNumber);
# rowPhoneData = phoneNumber.split('-');
numberData = phoneNumber.split('-')[0];
print(numberData);
# print(rowPhoneData);

# if(rowPhoneData[0] == "011"): print("Your number is SK Telecom");
# elif(rowPhoneData[0] == "016"): print("Your number is KT Telecom");
# elif(rowPhoneData[0] == "017"): print("Your number is Shinsegi Telecom");
# elif(rowPhoneData[0] == "018"): print("Your number is HANSOL Telecom");
# elif(rowPhoneData[0] == "019"): print("Your number is LG Telecom");
# elif(rowPhoneData[0] == "010"): print("All Telecoms");
# else: print("Error");

if(numberData == "011"): print("Your number is SK Telecom");
elif(numberData == "016"): print("Your number is KT Telecom");
elif(numberData == "017"): print("Your number is Shinsegi Telecom");
elif(numberData == "018"): print("Your number is HANSOL Telecom");
elif(numberData == "019"): print("Your number is LG Telecom");
elif(numberData == "010"): print("All Telecoms");
else: print("Error");
 """

""" 
postNumber = input("insert POST number : ");
for num in postNumber:
    print(num);

postNumberVor3 = postNumber[:3];

if(postNumberVor3 in ["010", "011", "012"]):
    print("Gang-Buk-gu");
elif(postNumberVor3 in ["013", "014", "015"]):
    print("Do-Bong-gu");
elif(postNumberVor3 in ["016", "017", "018"]):
    print("No-Won-gu");
elif(postNumberVor3 in ["019"]):
    print("Gang-Nam-gu");
else: print("Error");
 """
""" 
idNumber = input("insert ID : ");

rowDataIdNumber = idNumber.split("-");

print(rowDataIdNumber);
print(rowDataIdNumber[1]);
print(rowDataIdNumber[1][:1]);

genderNumber = rowDataIdNumber[1][:1];
if( genderNumber in ["2", "4"]): print("iD ", idNumber," Woman");
elif(genderNumber in ["1", "3"]): print("iD ", idNumber," Man");
else: print("They");
 """


""" 
idNumber = input("insert ID : ");
checkNumber = idNumber.split("-")[1][1:3];
print(checkNumber);
if(0 <= int(checkNumber) <= 8): print("Seoul");
else: print("Not Seoul");
 """

# 8 2 1 0 1 0 - 1 6 3 5 2 1 0
""" 
idNumber = input("input ID number : ");
print(idNumber);

totalNumber = int(idNumber[0] * 2) + int(idNumber[1] * 3) + int(idNumber[2] * 4)+ int(idNumber[3] * 5) + \
    int(idNumber[4] * 6) + int(idNumber[5] * 7) + int(idNumber[7] * 8) + int(idNumber[8] * 9) + \
    int(idNumber[9] * 2) + int(idNumber[10] * 3) + int(idNumber[11] * 4) + int(idNumber[12] * 5) ;

#check 1
print(totalNumber);
checkNumber = int(totalNumber) % 11 ;
print("Check Number 1 Process :",totalNumber,"% 11 = ",checkNumber);

checkSumNumber = 11 - int(checkNumber); 
print("Check Number 2 Process :","11 - ",checkNumber," = ", checkSumNumber);
print("End Number : ", idNumber[-1]);

#check2
if checkSumNumber == int(idNumber[-1]) : 
    print("Right Number");
else: 
    print("CheckSumNumber :",checkSumNumber);
    print("End Number :", idNumber[-1]);
    print("Wrong Number");
 """    

# https://api.bithumb.com/public/ticker/
# {
# "status":"0000",
# "data":
# {"opening_price":"58135000",
# "closing_price":"58167000",
# "min_price":"57897000",
# "max_price":"58252000",
# "units_traded":"90.58712715",
# "acc_trade_value":"5260554315.9905",
# "prev_closing_price":"58137000",
# "units_traded_24H":"1257.14835064",
# "acc_trade_value_24H":"73032766991.2193",
# "fluctate_24H":"-162000",
# "fluctate_rate_24H":"-0.28",
# "date":"1633281068757"}
# }
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 
# 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# Key Name	Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	최근 24시간 내 최저 거래금액
# max_price	최근 24시간 내 최고 거래금액

#requests.get().json()['data']
#btc.pop("name")
#btc["name"]
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc);
print(type(btc));
print(btc.keys());
print(btc.values());

opening_price = btc.pop("opening_price");
print("opening_price : ", opening_price) 

closing_price = btc.pop("closing_price");
print("closing_price", closing_price);

max_price = btc.pop("max_price");
print("max_price", max_price);

min_price = btc.pop("min_price");
print("min_price", min_price);

change_price = int(max_price) - int(min_price);

if ((int(opening_price) + int(change_price)) > int(max_price)): 
    print("UP Market");
else: 
    print("Down Market");

print(btc["units_traded"]);
print(btc.pop("units_traded"));