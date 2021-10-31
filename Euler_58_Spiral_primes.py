from utils import Timer
from utils import Fibonacci


@Timer.timeit
def main():
    i = 1
    prime_counter = 0
    counter = 1
    temp_counter = 0
    diagonal_num_counter = 0
    num = 7
    while diagonal_num_counter == 0 or prime_counter / diagonal_num_counter >= 0.1:
        num += 1
        while i <= num ** 2:
            if temp_counter == 4:
                counter += 1
                temp_counter = 0
            if Fibonacci.prime_or_not(i):
                prime_counter += 1
            diagonal_num_counter += 1

            i += 2 * counter
            temp_counter += 1

    print(num)

if __name__ == '__main__':
    main()

