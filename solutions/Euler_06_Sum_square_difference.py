from utils import Timer, Misc


# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is 385, The square of
# the sum of the first ten natural numbers is 3025, Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025-385 = 2640. Find the difference between the sum of the
# squares of the first one hundred natural numbers and the square of the sum.

@Timer.timeit
def main():
    # (1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4
    # 1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

    def square_of_sum_minus_sum_of_squares(n):
        return int(Misc.square_of_sums(n) - Misc.sum_of_squares(n))

    print(square_of_sum_minus_sum_of_squares(100))


if __name__ == '__main__':
    main()
