from utils import Timer, Primes
from math import sqrt

# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

@Timer.timeit
def main():
    def largest_prime_factor(number):
        for prime in list(Primes.primes_sieve_of_Eratosthenes(int((sqrt(number)))))[::-1]:
            if number % prime == 0:
                return prime
                break

    print('The largest prime factor of 600851475143 is', largest_prime_factor(600851475143))


if __name__ == '__main__':
    main()
