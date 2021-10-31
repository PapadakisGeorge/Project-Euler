from utils import Timer
from math import sqrt
import itertools


@Timer.timeit
def main():
    def number_decomposition(num):
        str_num = str(num)
        digits = []
        for i in range(0, len(str_num)):
            digits.append(int(str_num[i]))
        return digits

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

    def number_permutations(num):
        digits = number_decomposition(num)
        n_digits = len(digits)
        n_power = n_digits - 1
        return list(sorted([sum(v * (10**(n_power - i)) for i, v in enumerate(item)) \
                            for item in itertools.permutations(digits)]))


    def prime_permutations(num):
        prime_permutations = set()
        if prime_or_not(num):
            for i in number_permutations(num):
                if prime_or_not(i):
                    prime_permutations.add(i)
        return list(sorted(prime_permutations))

    def four_digit_prime_permutations(num):
        four_digit_prime_permutations = set()
        for i in prime_permutations(num):
            if len(str(i)) == len(str(num)):
               four_digit_prime_permutations.add(i)

        return list(sorted(four_digit_prime_permutations))

    def potential_steps(num):
        potential_steps = []
        for i in four_digit_prime_permutations(num):
            if i != num:
                if len(str(i - num)) == 4:
                    potential_steps.append(i - num)
        return potential_steps

    for num in range(1000, 9999):
        if prime_or_not(num):
            for step in potential_steps(num):
                if num + 2 * step in four_digit_prime_permutations(num):
                    print(str(num) + str(num + step) + str(num + 2 * step))









if __name__ == '__main__':
    main()

