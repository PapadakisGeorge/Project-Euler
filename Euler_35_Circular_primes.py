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

    def rotations(num):
        digits = number_decomposition(num)
        temp_rotations = []
        for i in range(len(digits)):
            digits.append(digits.pop(0))
            temp_rotations.append(digits[:])
        rotations = []
        for i in temp_rotations:
            temp = 0
            for j in range(0, len(i)):
                temp += i[j] * 10 ** (len(i) - 1 - j)
            rotations.append(temp)
        return rotations

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

    def circular_prime(num):
        flag = True
        if not prime_or_not(num):
            flag = print("The number", num, "is not a prime. Enter a prime")
        else:
            digits = number_decomposition(num)
            if 2 in number_decomposition(num):
                flag = False
            else:
                for i in rotations(num):
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
    for i in primes_to_million:
        if circular_prime(i):
            count += 1
            print(i)
    print(count)



if __name__ == '__main__':
    main()