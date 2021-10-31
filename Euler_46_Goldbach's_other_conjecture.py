from utils import Timer
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

    def Goldbach_conjecture_2(num):
        flag = False
        for p in SieveOfEratosthenes(num - 1):
            if int(sqrt((num - p) / 2)) == sqrt((num - p) / 2):
                flag = True
                break
        return flag

    flag = True
    n = 9
    while flag:
        if not prime_or_not(n) and n % 2 != 0:
            if not Goldbach_conjecture_2(n):
                flag = False
                print(n)
        n += 1



if __name__ == '__main__':
    main()

