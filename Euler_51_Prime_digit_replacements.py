from utils import Timer
from math import sqrt
import itertools


@Timer.timeit
def main():
    def prime_or_not(num):
        prime = True
        if num < 2:
            return False
        if num == 2:
            return True
        for factor in range(2, int(sqrt(num)) + 1):
            if num % factor == 0:
                prime = False
        return prime


    def SieveOfEratosthenes(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        primes = []
        for p in range(n + 1):
            if prime[p]:
                primes.append(p)
        primes.remove(0)
        primes.remove(1)
        return primes

    def digit_replacement(num, positions):
        replaced = []
        for dig in range(0, 10):
            temp = str(num)
            for i in positions:
                temp = temp.replace(temp[i], str(dig))
            if len(str(int(temp))) == len(str(num)):
                replaced.append(int(temp))
        return list(sorted(replaced))

    def different_positions(num):
        pos = []
        max_length = len(str(num))
        temp = ""
        for i in range(0, max_length):
            temp += str(i)
        for j in range(1, max_length):
            for k in list(itertools.combinations(temp, j)):
                pos.append(list(map(int, k)))
        return pos

    def prime_replacement(num, pos):
        final = digit_replacement(num, pos)
        for i in digit_replacement(num, pos):
            if not prime_or_not(i):
                final.remove(i)
        return list(sorted(final))

    primes = SieveOfEratosthenes(10**6)
    flag = True
    i = 0
    while flag:
        for p in different_positions(primes[i]):
            for num in prime_replacement(primes[i], p):
                if num in primes:
                    primes.remove(num)
            if len(prime_replacement(primes[i], p)) == 8:
                flag = False
                print(prime_replacement(primes[i], p)[0])
                break
        i += 1
if __name__ == '__main__':
    main()

