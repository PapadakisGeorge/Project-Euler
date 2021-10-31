import time


"""CHEAT
import datetime
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.datetime(y,m,1).weekday() == 6:
            count += 1
print(count)"""

start_time = time.time()

January = [str(i) + "Jan" for i in range(1, 32)]
February_28 = [str(i) + "Feb" for i in range(1, 29)]
February_29 = [str(i) + "Feb" for i in range(1, 30)]
March = [str(i) + "Mar" for i in range(1, 32)]
April = [str(i) + "Apr" for i in range(1, 31)]
May = [str(i) + "May" for i in range(1, 32)]
June = [str(i) + "Jun" for i in range(1, 31)]
July = [str(i) + "Jul" for i in range(1, 32)]
August = [str(i) + "Aug" for i in range(1, 32)]
September = [str(i) + "Sep" for i in range(1, 31)]
October = [str(i) + "Oct" for i in range(1, 32)]
November = [str(i) + "Nov" for i in range(1, 31)]
December = [str(i) + "Dec" for i in range(1, 32)]
calendar_1900 = January + February_28 + March + April + May + June + July + August + September + October + November +\
                        December
calendar = []
for i in range(0, 101):
    leap_counter = 0
    if leap_counter == 4:
        leap_counter = 0
        calendar = calendar + January + February_29 + March + April + May + June + July + August + September + October\
                   + November + December
    else:
        calendar = calendar + January + February_28 + March + April + May + June + July + August + September + October\
                   + November + December
    leap_counter += 1

for i in range(0, len(calendar)):
    calendar[i] += str(i % 7)

for i in range(0, len(calendar_1900)):
    calendar_1900[i] += str(i % 7)


counter = 0
set = ["1Jan6", "1Feb6", "1Mar6", "1Apr6", "1May6", "1Jun6", "1Jul6", "1Aug6", "1Sep6", "1Oct6", "1Nov6", "1Dec6"]
for i in range(0, len(calendar)):
    if calendar[i] in set:
            counter += 1
counter_1900 = 0

for i in range(0, len(calendar_1900)):
        if calendar[i] in set:
                counter_1900 += 1
print(counter - counter_1900)





print("--- %s seconds ---" % (time.time() - start_time))