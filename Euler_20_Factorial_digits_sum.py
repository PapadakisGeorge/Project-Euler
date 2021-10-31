import time
import math



start_time = time.time()


def number_decomposition(num):
    str_num = str(num)
    digits = []
    for i in range(0, len(str_num)):
        digits.append(int(str_num[i]))
    return digits


fact_s = 0
for i in range(0, len(number_decomposition(math.factorial(100)))):
    fact_s += number_decomposition(math.factorial(100))[i]
print(fact_s)



print("--- %s seconds ---" % (time.time() - start_time))