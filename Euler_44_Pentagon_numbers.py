from utils import Timer
from math import sqrt



@Timer.timeit
def main():

    def pentagon_or_not(num):
        if sqrt(1 + 24 * num) == int(sqrt(1 + 24 * num)):
            if (int(sqrt(1 + 24 * num)) + 1) % 6 == 0:
                return True
        else:
            return False

    flag = True
    i = 1
    while flag:
        for j in range(1, i):
            a = int(i * (3 * i - 1) / 2)
            b = int(j * (3 * j - 1) / 2)
            if pentagon_or_not(a + b) and pentagon_or_not(a - b):
                print(a, b, a - b)
                flag = False
                break
        i += 1


if __name__ == '__main__':
    main()

