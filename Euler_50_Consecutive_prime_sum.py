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

    L = 1000000
    prime_sum = [0]
    for p in SieveOfEratosthenes(int(L / 100)):
        prime_sum.append(prime_sum[-1] + p)
        if prime_sum[-1] >= L:
            break
    c = len(prime_sum)

    terms = 1
    for i in range(c):
        for j in range(c - 1, i + terms, -1):
            n = prime_sum[j] - prime_sum[i]
            if j - i > terms and prime_or_not(n):
                terms, max_prime = j - i, n
                break

    print(max_prime)










if __name__ == '__main__':
    main()

