from utils import Timer
from math import factorial

@Timer.timeit
def main():
    def number_decomposition(num):
        str_num = str(num)
        digits = []
        for i in range(0, len(str_num)):
            digits.append(int(str_num[i]))
        return digits

    def curious_number(num):
        s = 0
        for i in range(0, len(number_decomposition(num))):
            s += factorial(number_decomposition(num)[i])
        if num == s:
            return True
        else:
            return False
    s = 0
    for i in range(10, 99999):
        if curious_number(i):
            s += i
    print(s)

if __name__ == '__main__':
    main()