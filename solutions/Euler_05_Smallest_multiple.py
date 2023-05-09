from utils import Timer, Number_Theory_Misc


# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

@Timer.timeit
def main():
    print(Number_Theory_Misc.lowest_common_denominator_multiple(11, 12, 13, 14, 15, 16, 17, 18, 19, 20))


if __name__ == '__main__':
    main()
