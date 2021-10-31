from utils import Timer
from utils import Fibonacci

@Timer.timeit
def main():

    def number_reversal(num):
        return int(str(num)[::-1])

    def Lychrel_or_not(num):
        counter = 0
        num += number_reversal(num)
        while not Fibonacci.palindromic_number(num) and counter < 50:
            num += number_reversal(num)
            counter += 1
        if Fibonacci.palindromic_number(num):
            return False
        else:
            return True
    Lychrel_total = 0
    for num in range(1, 10000):
        if Lychrel_or_not(num):
            Lychrel_total += 1
    print(Lychrel_total)










if __name__ == '__main__':
    main()

