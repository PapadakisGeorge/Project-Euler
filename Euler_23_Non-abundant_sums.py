from math import sqrt
import time
def main():

    start_time = time.time()


    def sum_of_divisors(num):
        s = 1
        t = sqrt(num)
        for i in range(2, int(t) + 1):
            if num % i == 0:
                s += i + num / i
        if t == int(t):
            s -= t
        return s

    limit = 28123
    s = 0
    abundant_numbers = set()
    for n in range(1, limit):
        if sum_of_divisors(n) > n:
            abundant_numbers.add(n)
        if not any((n - a in abundant_numbers) for a in abundant_numbers):
            s += n
    print(s)





    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()