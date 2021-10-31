from utils import Timer
import math
from functools import lru_cache


@Timer.timeit
def main():
    def s(n):
        first_digit = str(n % 9)
        x = n // 9
        last_digits = "9" * x

        return int(first_digit + last_digits)

    def S(n, acc=0):
        while True:
            if n == 1:
                return s(1) + acc
            (n, acc) = (n - 1, acc + s(n))
            continue

    def S_tail(i, j):
        x = 0
        if i > j:
            print("Incorrect inputs")
        else:
            for k in range(i, j + 1):
                x += s(k)
        return x

    def fibonacci_seq(n):
        l_1 = (1 + math.sqrt(5)) / 2
        l_2 = (1 - math.sqrt(5)) / 2
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return round((l_1 ** n + l_2 ** n) / math.sqrt(5))

    @lru_cache(maxsize=1)
    def Final_Sum(n):
        if n == 2:
            return S(2)
        else:
            return Final_Sum(n - 1) + S(fibonacci_seq(n))

    print(Final_Sum(25) % 1000000007)


if __name__ == '__main__':
    main()
