# threeInTime
# Brute Forceing

timeNumber = int(input());

countThreeInTime = 0;

for hour in range(timeNumber + 1): # 1-> 2 -> 1:59
    for min in range(60): # 60 minute
        for sec in range(60): # 60 second
            # print(str(hour) + str(min) + str(sec));
            if '3' in str(hour) + str(min) + str(sec):
                countThreeInTime += 1;
                print("3 in :", str(hour) + str(min) + str(sec));

print("total:", countThreeInTime);
