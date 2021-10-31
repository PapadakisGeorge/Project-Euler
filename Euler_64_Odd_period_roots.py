from utils import Timer
from itertools import permutations
import numpy as np
from collections import Counter
import math


@Timer.timeit
def main():
    def continued_fraction(n):

        m = [0]
        d = [1]
        a = [int((math.sqrt(n)))]

        def terminate():
            for i in range(len(a) - 1):
                if m[i] == m[-1] and d[i] == d[-1] and a[i] == a[-1]:
                    return True
            return False

        while not terminate():
            m.append(d[-1] * a[-1] - m[-1])
            d.append((n - m[-1] ** 2) / d[-1])
            a.append(int(((math.sqrt(n) + m[-1]) / d[-1])))

        return len(a) - 2  

    print(sum(continued_fraction(n) % 2 == 1
              for n in range(1, 10000 + 1)
              if int(math.sqrt(n)) != math.sqrt(n)))


if __name__ == '__main__':
    main()
