from utils import Timer
from utils import Fibonacci

@Timer.timeit
def main():

    largest = 0
    for a in range(0, 100):
        for b in range(0, 100):
            s = 0
            for i in Fibonacci.number_decomposition(a ** b):
                s += i
            if s > largest:
                largest = s
    print(largest)










if __name__ == '__main__':
    main()

