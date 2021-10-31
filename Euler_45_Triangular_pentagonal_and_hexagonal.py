from utils import Timer
from math import sqrt
import itertools


@Timer.timeit
def main():
    def triangle_num_to(n):
        def triangle_num():
            n = 1
            while True:
                yield int(n*(n+1)/2)
                n += 1
        first_n = list(itertools.islice(triangle_num(), n))
        return first_n

    def pentagon_or_not(num):
        if sqrt(1 + 24 * num) == int(sqrt(1 + 24 * num)):
            if (int(sqrt(1 + 24 * num)) + 1) % 6 == 0:
                return True
        else:
            return False

    def hexagonal_or_not(num):
        if int((sqrt(8 * num + 1) + 1) / 4) == (sqrt(8 * num + 1) + 1) / 4:
            return True
        else:
            return False

    def test(num):
        if pentagon_or_not(num) and hexagonal_or_not(num):
            return True
        else:
            return False

    flag = True

    while flag:
        for num in triangle_num_to(10**6):
            if num != 1 and num != 40755:
                if test(num):
                    flag = False
                    print(num)
                    break



if __name__ == '__main__':
    main()

