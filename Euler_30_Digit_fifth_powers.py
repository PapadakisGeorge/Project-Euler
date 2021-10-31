import time


def main():
    start_time = time.time()

    def number_decomposition(num):
        str_num = str(num)
        digits = []
        for i in range(0, len(str_num)):
            digits.append(int(str_num[i]))
        return digits

    def power_of_digits(a, n):
        digits = number_decomposition(a)
        s = 0
        for i in range(0, len(digits)):
            s += digits[i]**n
        if s == a:
            return True
        else:
            return False


    s = 0
    for i in range(10, 531441):
        if power_of_digits(i, 5):
            s += i
    print(s)



    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()