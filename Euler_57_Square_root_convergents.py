from utils import Timer
from utils import Fibonacci
from fractions import Fraction
import itertools
@Timer.timeit
def main():

    def square_root_fract(n):
        fract = [Fraction(1 + 1 / 2)]
        i = 1
        while i <= n:
            temp = 1 + 1 / (1 + fract[i - 1])
            fract.append(temp)
            i += 1
            temp = 0
        return fract

    counter = 0
    for i in square_root_fract(1000):
        if len(str(i.numerator)) > len(str(i.denominator)):
            counter += 1
    print(counter)










if __name__ == '__main__':
    main()

