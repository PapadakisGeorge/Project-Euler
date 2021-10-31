import time


start_time = time.time()


def digit_sum(num):
    num_string = str(num)
    digits_in_lst = [int(num_string[i]) for i in range(len(num_string))]
    s_digits = 0
    for i in digits_in_lst:
        s_digits += i
    return s_digits
print(digit_sum(2**1000))


print("--- %s seconds ---" % (time.time() - start_time))