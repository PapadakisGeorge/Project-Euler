from utils import Timer
import itertools

@Timer.timeit
def main():

    def pandigital(num):
        if len(str(num)) == 10:
            if ''.join(sorted(list(str(num)))) == "0123456789":
                return True
        else:
            return False


    def divisibility_property(num):
        primes = [2, 3, 5, 7, 11, 13, 17]
        num_str = str(num)
        flag = True
        if pandigital(num):
            for i in range(1, 8):
                if int(num_str[i: i + 3]) % primes[i - 1] != 0:
                    flag = False
                    break
        else:
            flag = False
        return flag
    s = 0

    pandigitals = [''.join(i) for i in itertools.permutations("0123456789")]
    pandigitals = map(int, pandigitals)
    for i in pandigitals:
        if divisibility_property(i):
            s += i

    print(s)

if __name__ == '__main__':
    main()