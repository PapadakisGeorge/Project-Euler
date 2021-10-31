import time
import sys

try:
    start_time = time.time()


    def triangular(n):
        n_th_triangular = 0
        for i in range(0, n + 1):
            n_th_triangular += i
        return n_th_triangular


    def tau(n):
        sqroot, t = int(n ** 0.5), 0
        for factor in range(1, sqroot + 1):
            if n % factor == 0:
                t += 2
        if sqroot * sqroot == n:
            t = t - 1
        return t


    n = triangular(1)
    while tau(triangular(n)) <= 500:
        n += 1

    print(n, triangular(n))

except TypeError:
    print("You did not insert a valid number...")
    sys.exit()
except UnboundLocalError:
    print("You did not insert a valid number...")
    sys.exit()

print("--- %s seconds ---" % (time.time() - start_time))