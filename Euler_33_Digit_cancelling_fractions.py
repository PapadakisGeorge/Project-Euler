from utils import Timer
from fractions import Fraction


@Timer.timeit
def main():

    def curious_division(num_1, num_2):
        if num_1 != num_2:
            if len(str(num_1)) == 2 and len(str(num_2)) == 2:
                if str(num_1)[1] != "0" and str(num_2)[1] != "0":
                    if str(num_1)[0] == str(num_2)[0]:
                        return Fraction(int(str(num_1)[1]), int(str(num_2)[1]))
                    elif str(num_1)[1] == str(num_2)[0]:
                        return Fraction(int(str(num_1)[0]), int(str(num_2)[1]))
                    elif str(num_1)[0] == str(num_2)[1]:
                        return Fraction(int(str(num_1)[1]), int(str(num_2)[0]))
                    elif str(num_1)[1] == str(num_2)[1]:
                        return Fraction(int(str(num_1)[0]), int(str(num_2)[0]))
                    else:
                        return 0
                elif str(num_1)[1] == "0" or str(num_2)[1] == "0":
                    if str(num_1)[0] == str(num_2)[0]:
                        return 0
                    elif str(num_1)[1] == str(num_2)[0]:
                        return 0
                    elif str(num_1)[0] == str(num_2)[1]:
                        return 0
                    elif str(num_1)[1] == str(num_2)[1]:
                        return 0
                    else:
                        return 0
        else:
            return 0

    numera = 1
    denom = 1
    i = 11
    while i <= 99:
        for j in range(i, 100):
            if curious_division(i, j) == Fraction(i, j):
                print(i,"/",j,"=",curious_division(i,j) )
                numera *= i
                denom *= j
        i += 1

    print(Fraction(numera, denom).denominator)
if __name__ == '__main__':
    main()