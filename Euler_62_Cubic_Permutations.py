from utils import Timer
from itertools import permutations
import numpy as np
from collections import Counter

@Timer.timeit
def main():
    def cubes(n):
        cubes = []
        num = 1
        while num <= n:
            cubes.append(num ** 3)
            num += 1
        return cubes

    def digit_permutations(num):
        digit_perms = {''.join(p) for p in permutations(str(num))}
        return map(int, digit_perms)

    def cubic_permutations(num):
        counter = 0
        for i in digit_permutations(num):

            if i ** (1 / 3) - np.fix(i ** (1 / 3)) > 0.99999999999:
                counter += 1
        return counter

    def number_decomposition(num):
        digits = []
        for i in str(num):
            digits.append(int(i))
        return list(sorted(digits))

    cube_list = cubes(10000)
    decomposed_cube_list = list(map(number_decomposition, cube_list))
    result = None
    while result is None:
        for i in decomposed_cube_list:

            if decomposed_cube_list.count(i) == 5:
                result = decomposed_cube_list.index(i) + 1
                break
            else:
                continue
    print(result ** 3)


if __name__ == '__main__':
    main()
