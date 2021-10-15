#021_050 String
#파이썬 스트링은 수정 되지않고
#새로운 문자열 객체가 반환

titles = "python";
print(len(titles));

print(titles[0]);
print(titles[1]);
print(titles[2]);
print(titles[3]);
print(titles[4]);
print(titles[5]);

# p,t 
# separator sep=''
print(titles[0], titles[2], sep="/");

# slice string 
# string[]
license_plate = "MS X1999";
print(len(license_plate));
# 1999
print(license_plate[0]);
print(license_plate[0:]);
print(license_plate);
print(license_plate[-1:]);
print(license_plate[-2:]);
print(license_plate[-3:]);
print(license_plate[-4:]);
print(license_plate[-5:]);

string_RL = "RLRLRLRLRL";
# RRRRR
print(string_RL);
print(string_RL[0]);
print(string_RL[2]);
print(string_RL[4]);
print(string_RL[6]);
print(string_RL[8]);
# print(string_RL[10]);//string index out of range

# string[start : end : offset]
print( string_RL[0:9:2]);
print( string_RL[0:20:2]);

BigString = "Python";
print(BigString);
print(len(BigString));

# reverseString[::-1];
print(BigString[::-1]);

phone_number = "49-555-5555";
print(phone_number[::-1]);
print(phone_number);

#string replace Method 
#string.replace('-','');
print(phone_number.replace('-',''));
print(phone_number);
phone_replace = phone_number.replace('-','*');
print(phone_replace);
print(phone_replace.replace('*',''));

urlAddress = "https://www.google.de";
print(urlAddress);
print(urlAddress[-2:]);
print(urlAddress);

# String Split
# string.split('.');
# The replace() method returns a copy of the string where 
# the old substring is replaced with the new substring. 
# The original string is unchanged.
urlSplit = urlAddress.split('.');
print(urlSplit);
print(urlSplit[-1]);

welcomHome = "Hello WWW";
#split()
print(welcomHome);
print(welcomHome.split());
print(welcomHome.split(' '));

underbarString = "Big_Small";
print(underbarString.split('_'));

date = "2021-05-01";
noHyphen = date.split('-');
print(noHyphen);

leftDate = "2021-09-01     ";
centerDate1 = leftDate.rsplit();
print(centerDate1);

rightDate = "     2021-09-30";
centerDate2 = rightDate.rsplit();
print(centerDate2);

#replace()
AaString = "abcdfe2a354a32a";
print(AaString.replace('a','A'));
print(AaString);

a = 3;
b = 4;
print(a + b);

print("Hi " * 3);

print("-" * 80);

text1 = "Python";
text2 = "Algorithm";

print((text1, text2) * 4);
text3 = text1 + ' ' + text2 + ' ';
print(text3 * 4);

name1 = "John";
age1 = 23;

name2 = "Jack";
age2 = 31;

print("Name : " , name1,"Age : ",age1 );
print("Name : " , name2,"Age : ",age2 );

# %fomatting
print("Name %s : Age %d " %(name1, age1));
print("Name %s : Age %d " %(name2, age2));

# format
print("Name : {} Age : {}" .format(name1, age2));
print("Name : {} Age : {}" .format(name2, age2));

#f-string
print(f"Name : {name1} Age : {age1}");
print(f"Name : {name2} Age : {age2}");

#replace()
samsungStock = "5,478,329,590";
print(samsungStock);
print(type(samsungStock.replace(',','')));
print(type(int(samsungStock.replace(',',''))));
print(type(samsungStock));

quarter = "2020/03(E) (IFRS연결)";
print(quarter);

# split()
quarterSplit = quarter.split('(');
print(quarterSplit);
print(quarterSplit[-3]);

# String slice
print(quarter[:10]);

#replace()
spaceWithString = " SAMSUNG ";
noSpaceWithString = " SAMSUNG ".replace(" ","");
print(noSpaceWithString);

#strip() whitespace remove
print(spaceWithString.strip());

# upper() string
smallTicker = "btc_krw";
print(smallTicker.upper());

# lower() string
bigTicker = "BTC_KRW";
print(bigTicker.lower());

# capitalize() string first Big, rest small
welcom = "hello World";
print(welcom.capitalize());

file1Name = "programming.doc";
file2Name = "algorithm.xlsx";

docFile1= file1Name.endswith(('doc', 'docx'));
print(f"Result : {docFile1}");

docFile2 = file2Name.endswith(('doc', 'docx'));
print(f"Result : {docFile2}");

docFile3 = welcom.endswith("World",6,11);
print(f"Result : {docFile3}");

