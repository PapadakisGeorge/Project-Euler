from utils import Timer
from math import sqrt


@Timer.timeit
def main():
    def number_decomposition(num):
        str_num = str(num)
        digits = []
        for i in range(0, len(str_num)):
            digits.append(int(str_num[i]))
        return digits

    def left_reductions(num):
        digits = number_decomposition(num)
        temp_red = []
        for i in range(len(digits)-1):
            del digits[-1]
            temp_red.append(digits[:])
        left_reduction = []
        for i in temp_red:
            temp = 0
            for j in range(0, len(i)):
                temp += i[j] * 10 ** (len(i) - 1 - j)
            left_reduction.append(temp)
        return left_reduction

    def right_reductions(num):
        digits = number_decomposition(num)
        temp_red = []
        for i in range(len(digits)-1):
            del digits[0]
            temp_red.append(digits[:])
        right_reduction = []
        for i in temp_red:
            temp = 0
            for j in range(0, len(i)):
                temp += i[j] * 10 ** (len(i) - 1 - j)
            right_reduction.append(temp)
        return right_reduction

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

    def right_truncatable_prime(num):
        flag = True
        if not prime_or_not(num):
            flag = False
            print("The number", num, "is not a prime. Enter a prime")
        else:
            digits = number_decomposition(num)
            if len(digits) == 1:
               flag = print("A one_digit number is not truncatable.")
            else:
                for i in right_reductions(num):
                    if not prime_or_not(i):
                        flag = False
                        break
        return flag

    def left_truncatable_prime(num):
        flag = True
        if not prime_or_not(num):
            flag = False
            print("The number", num, "is not a prime. Enter a prime")
        else:
            digits = number_decomposition(num)
            if len(digits) == 1:
               flag = print("A one_digit number is not truncatable.")
            else:
                for i in left_reductions(num):
                    if not prime_or_not(i):
                        flag = False
                        break
        return flag

    def SieveOfEratosthenes(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        primes = []
        for p in range(n + 1):
            if prime[p]:
                primes.append(p)
        primes.remove(0)
        primes.remove(1)
        return primes
    primes_to_million = SieveOfEratosthenes(10**6)

    count = 0
    s = 0
    for i in primes_to_million:
        if right_truncatable_prime(i) and left_truncatable_prime(i):
            s += i
    print(s)


if __name__ == '__main__':
    main()