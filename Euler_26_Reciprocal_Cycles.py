from decimal import *
import time
from math import gcd

def main():
    start_time = time.time()
    reccuring_circles =[]
#If a number d is not coprime with 10, 1/d has not the largest circle
    for d in range(2, 1000):
        if gcd(10, d) == 1:
#We are looking for the multiplicative order of d modulo 10
            i = 1
            while 10**i % d != 1:
                i += 1
            reccuring_circles.append(i)
        else:
            reccuring_circles.append(0)
    print(reccuring_circles.index(max(reccuring_circles))+2)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()