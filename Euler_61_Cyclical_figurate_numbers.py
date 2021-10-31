from utils import Timer
from itertools import permutations

@Timer.timeit
def main():

    global s

    def triangle_numbers(n):
        return n * (n + 1) / 2
    flag = True
    i = 1
    four_digit_triangle_numbers = []
    while flag:
        if triangle_numbers(i)>= 1000 and triangle_numbers(i) <= 9999:
            four_digit_triangle_numbers.append(int(triangle_numbers(i)))
        i += 1
        if triangle_numbers(i) > 9999:
            flag = False

    def square_numbers(n):
        return n ** 2

    four_digit_triangle_numbers = tuple(four_digit_triangle_numbers)

    flag = True
    i = 1
    four_digit_square_numbers = []
    while flag:
        if square_numbers(i) >= 1000 and square_numbers(i) <= 9999:
            four_digit_square_numbers.append(int(square_numbers(i)))
        i += 1
        if square_numbers(i) > 9999:
            flag = False
    four_digit_square_numbers = tuple(four_digit_square_numbers)

    def pentagonal_numbers(n):
        return n * (3 * n - 1) / 2

    flag = True
    i = 1
    four_digit_pentagonal_numbers = []
    while flag:
        if pentagonal_numbers(i) >= 1000 and pentagonal_numbers(i) <= 9999:
            four_digit_pentagonal_numbers.append(int(pentagonal_numbers(i)))
        i += 1
        if pentagonal_numbers(i) > 9999:
            flag = False
    four_digit_pentagonal_numbers = tuple(four_digit_pentagonal_numbers)

    def hexagonal_numbers(n):
        return n * (2 * n - 1)

    flag = True
    i = 1
    four_digit_hexagonal_numbers = []
    while flag:
        if hexagonal_numbers(i) >= 1000 and hexagonal_numbers(i) <= 9999:
            four_digit_hexagonal_numbers.append(int(hexagonal_numbers(i)))
        i += 1
        if hexagonal_numbers(i) > 9999:
            flag = False
    four_digit_hexagonal_numbers = tuple(four_digit_hexagonal_numbers)

    def heptagonal_numbers(n):
        return n * (5 * n -3) / 2

    flag = True
    i = 1
    four_digit_heptagonal_numbers = []
    while flag:
        if heptagonal_numbers(i) >= 1000 and heptagonal_numbers(i) <= 9999:
            four_digit_heptagonal_numbers.append(int(heptagonal_numbers(i)))
        i += 1
        if heptagonal_numbers(i) > 9999:
            flag = False

    four_digit_heptagonal_numbers = tuple(four_digit_heptagonal_numbers)

    def octagonal_numbers(n):
        return n * (3 * n - 2)

    flag = True
    i = 1
    four_digit_octagonal_numbers = []
    while flag:
        if 1000 <= octagonal_numbers(i) <= 9999:
            four_digit_octagonal_numbers.append(int(octagonal_numbers(i)))
        i += 1
        if octagonal_numbers(i) > 9999:
            flag = False

    four_digit_octagonal_numbers = tuple(four_digit_octagonal_numbers)

    def cyclical(n, m, flag=True):
        if str(n)[-2:] != str(m)[:2]:
                flag = False
        return flag

    s = None
    a = [1, 2, 3, 4, 5, 6]
    perm = set(permutations(a))
    four_digits = {1: four_digit_square_numbers,
                   2: four_digit_triangle_numbers,
                   3: four_digit_pentagonal_numbers,
                   4: four_digit_hexagonal_numbers,
                   5: four_digit_heptagonal_numbers,
                   6: four_digit_octagonal_numbers
                   }
    result = None

    while result is None:
        for tup in perm:
            for n_1 in four_digits[tup[0]]:
                for n_2 in four_digits[tup[1]]:
                    if cyclical(n_1, n_2):
                        for n_3 in four_digits[tup[2]]:
                            if cyclical(n_2, n_3):
                                for n_4 in four_digits[tup[3]]:
                                    if cyclical(n_3, n_4):
                                        for n_5 in four_digits[tup[4]]:
                                            if cyclical(n_4, n_5):
                                                for n_6 in four_digits[tup[5]]:
                                                    if cyclical(n_5, n_6) and cyclical(n_6, n_1):
                                                        result = (n_1, n_2, n_3, n_4, n_5, n_6)
                                                        s = 0

    for i in result:
        s += i
    print(s)


if __name__ == '__main__':
    main()
