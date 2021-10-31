import time
from math import sqrt



start_time = time.time()


def sum_of_divisors(num):
    s = 1
    t = sqrt(num)
    for i in range(2, int(t) + 1):
        if num % i == 0:
            s += i + num / i
    if t == int(t):
        s -= t
    return int(s)
divisor_s_lst = []


for i in range(1, 10000):
    divisor_s_lst.append({i, sum_of_divisors(i)})

s_amicable = 0
for i in range(0, len(divisor_s_lst)):
    for j in range(i + 1, len(divisor_s_lst)):
        if divisor_s_lst[i] == divisor_s_lst[j]:
            for k in divisor_s_lst[i]:
                s_amicable += k
                print(k, s_amicable)
print(s_amicable)


print("--- %s seconds ---" % (time.time() - start_time))