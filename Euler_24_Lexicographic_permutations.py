import time
import itertools
from math import factorial
def main():

    start_time = time.time()
    digits = [i for i in range(0, 10)]
    permutations = [i for i in itertools.permutations(digits)]

    num = 0
    for dig in range(0, len(permutations[10**6 - 1])):
        num += 10**(9 - dig)*permutations[10**6 -1][dig]
    print(num)







    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()