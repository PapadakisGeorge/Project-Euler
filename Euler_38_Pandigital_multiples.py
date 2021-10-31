from utils import Timer
from math import sqrt


@Timer.timeit
def main():


    def pandigital(num):
        if len(str(num)) == 9:
            if ''.join(sorted(list(str(num)))) == "123456789":
                return True
        else:
            return False

    def concatenated_product(num, n):
        str_conc_prod = ""
        for i in range(1, n + 1):
            str_conc_prod += str(num * i)
        return int(str_conc_prod)

    def concatenated_pandigital(num, n):
        if pandigital(concatenated_product(num, n)):
            return True
        else:
            return False

    for j in range(1, 10000):
        for i in range(2, 10):
            if concatenated_pandigital(j, i):
                    largest = concatenated_product(j, i)
    print(largest)




if __name__ == '__main__':
    main()