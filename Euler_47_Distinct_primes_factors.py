from utils import Timer



@Timer.timeit
def main():
    def prime_factors(num):
        factors = set()
        d = 2
        while num > 1:
            while num % d == 0:
                factors.add(d)
                num /= d
            d = d + 1
            if d * d > num:
                if num > 1:
                    factors.add(int(num))
                break
        return factors

    def number_of_distinct_prime_factors(num):
        return len(prime_factors(num))

    flag = True
    num = 1
    while flag:
        if number_of_distinct_prime_factors(num) == 4 and number_of_distinct_prime_factors(num + 1) == 4 and\
                number_of_distinct_prime_factors(num + 2) == 4 and number_of_distinct_prime_factors(num + 3) == 4:
            flag = False
            print(num)
        num += 1


if __name__ == '__main__':
    main()

