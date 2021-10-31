from utils import Timer
from math import factorial

@Timer.timeit
def main():
    def combinations(n, k):
        return factorial(n) / (factorial(k) * factorial(n - k))

    counter = 0
    for n in range(1, 101):
        for k in range(1, n):
            if combinations(n, k) > 10 ** 6:
                counter += 1
    print(counter)













if __name__ == '__main__':
    main()

