#051_070 list
# 파이선 리스트는 순서가 있고 
# 수정 가능한 자료구조

from functools import total_ordering
from typing import Sized

#len list length
moveRanking = ["Spyder Man", "Doom", "TENET"];
print(moveRanking);
print(len(moveRanking))
print(moveRanking[0]);
print(moveRanking[1]);
print(moveRanking[2]);
# print(moveRanking[3]); //list index out of range

# moveRanking[3] = "Bat Man";
# print(moveRanking[3])
# print(moveRanking + "Bat Man");

#append() add object to end
moveRanking.append("BAT Man");
print(len(moveRanking));
print(moveRanking);

#insert(index, object) 
moveRanking.insert(1, "Super Man");
print(moveRanking);
print(len(moveRanking));

#pop(index)
moveRanking.pop(3);
print(moveRanking);
print(len(moveRanking));

#del
del moveRanking[1];
print(moveRanking);
print(len(moveRanking));

del moveRanking[2];
del moveRanking[0];
print(moveRanking);
print(len(moveRanking));

lang1 = ["C", "C++", "JAVA"];
lang2 = ["Python", "Go", "C#"];
print(lang1);
print(lang2);
lang1.append(lang2);
print(lang1);
print(len(lang1));
del lang1[3];
print(lang1);
lang3 = lang1 + lang2 ;
print(len(lang3));
print(lang3);

nums = [1, 2, 3, 4, 5];
print(nums);
totalNums = sum(nums);
print(totalNums);
print(len(nums));
average = totalNums / len(nums);
print(average);

#sliceing [ : : ]
dailyPrice = ['20180728', 100, 130, 140, 150, 160, 170];
print(dailyPrice);
print(dailyPrice[:1]);
print(dailyPrice[1:]);
print(dailyPrice[-6:]);

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print(nums[1::2]);
print(nums[1:10:2]);

reversNums = [1, 2, 3, 4, 5];
print(reversNums);
# print(reversNums[5:0:-1]);
print(reversNums[::-1]);

company = ['Naver', 'LG', 'SAMSUNG'];
print(company);
del company[1];
print(company);
print(company[0], company[1]);

# join()
company.append('Kakao');
print("/".join(company));
print("-".join(company));
print(" ".join(company));

#split()
slashWithString = "SAMSUNG/LG/Naver";
noSlashWithString = slashWithString.split("/");
print(noSlashWithString);

#sort() 
numData1 = [2, 4, 3, 1, 5, 10, 9];
numData1.sort();
print(numData1);

# sorted()
numData2 = [3, 4, 7, 0, 6, 8, 2];
sortNumData = sorted(numData2);
print(sortNumData);


