from utils import Timer
from itertools import permutations
from math import sqrt

@Timer.timeit
def main():
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

    def pandigital(num):
        if len(str(num)) == 9:
            if ''.join(sorted(list(str(num)))) == "123456789":
                return True
        if len(str(num)) == 8:
            if ''.join(sorted(list(str(num)))) == "12345678":
                return True
        if len(str(num)) == 7:
            if ''.join(sorted(list(str(num)))) == "1234567":
                return True
        if len(str(num)) == 6:
            if ''.join(sorted(list(str(num)))) == "123456":
                return True
        if len(str(num)) == 5:
            if ''.join(sorted(list(str(num)))) == "12345":
                return True
        if len(str(num)) == 4:
            if ''.join(sorted(list(str(num)))) == "1234":
                return True
        if len(str(num)) == 3:
            if ''.join(sorted(list(str(num)))) == "123":
                return True
        if len(str(num)) == 2:
            if ''.join(sorted(list(str(num)))) == "12":
                return True
        else:
            return False
    largest = 0
    for i in list(reversed(SieveOfEratosthenes(10**8))):
        if pandigital(i):
            largest = i
            break
    print(largest)

if __name__ == '__main__':
    main()