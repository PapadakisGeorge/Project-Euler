from utils import Timer
from utils import Fibonacci
import sys


@Timer.timeit
def main():
    def Prime_pair_sets(primes, p):
        flag = True
        for i in primes:
            if p == i:
                flag = False
            elif not Fibonacci.prime_or_not(int(str(i) + str(p))) or not Fibonacci.prime_or_not(int(str(p) + str(i))):
                flag = False
                break
        return flag

    potential_set = [3, 7, 109, 673]
    for p in Fibonacci.SieveOfEratosthenes(10 ** 7):
        if Prime_pair_sets(potential_set, p):
            potential_set.append(p)
            print(potential_set)
            break


if __name__ == '__main__':
    main()
