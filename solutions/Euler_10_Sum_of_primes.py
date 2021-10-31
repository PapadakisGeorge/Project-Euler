from utils import Timer, Primes


# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

@Timer.timeit
def main():
    def primes_sum(limit):
        result = 2
        for candidate in range(3, limit, 2):
            if Primes.find_primes(candidate):
                result += candidate
        return result

    print('The sum of all the primes below two million is:', primes_sum(2 * 1000000))


if __name__ == '__main__':
    main()
