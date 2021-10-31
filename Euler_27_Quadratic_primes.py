from math import sqrt
import time
def main():
    start_time = time.time()
    def SieveOfEratosthenes(n):

        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        primes = []
        for p in range(n + 1):
            if prime[p]:
                primes.append(p)
        return primes

    def prime_or_not(num):
        prime = True
        if num < 2:
            return False
        if num == 2:
            return True
        for factor in range(1, int(sqrt(num)) + 1):
            if num % factor == 0:
                prime = False
        return prime

    primes_until_100 = SieveOfEratosthenes(1000)
    longest_count = 0
    longest_prod = 1
    for a in range(-999, 1001, 2):
        for i in range(0, len(primes_until_100)):
                b = primes_until_100[i]
                n = 0
                while prime_or_not(n**2 + a * n + b):
                    n += 1
                if longest_count < n:
                    longest_prod = a * b
                    longest_count = n
    print(longest_prod)

    print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == '__main__':
    main()