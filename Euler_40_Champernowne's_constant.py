from utils import Timer
from math import sqrt


@Timer.timeit
def main():
    champ_temp = ""
    for i in range(1, 10 ** 6):
        champ_temp += str(i)
    champ = champ_temp[0:1000000]

    prod = int(champ[0]) * int(champ[9]) * int(champ[99]) * int(champ[999]) * int(champ[9999]) * int(
        champ[99999]) * int(champ[999999])
    print(prod)




if __name__ == '__main__':
    main()