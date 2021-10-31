from utils import Timer

@Timer.timeit
def main():
    def number_decomposition(num):
        str_num = str(num)
        digits = []
        for i in range(0, len(str_num)):
            digits.append(int(str_num[i]))
        return list(sorted(digits))

    flag = True
    i = 1
    while flag:
        if number_decomposition(i) == number_decomposition(2*i) and number_decomposition(2* i) ==\
            number_decomposition(3*i) and number_decomposition(i) == number_decomposition(4*i) and \
                number_decomposition(i) == number_decomposition(5 * i) and number_decomposition(i) ==\
                number_decomposition(6*i):
            print(i)
            flag = False
        i += 1














if __name__ == '__main__':
    main()

