import time
import sys

try:
    start_time = time.time()
    def Collatz_sequence_lenght(num):
        collatz_length = 1
        while not num == 1:
            if num % 2 == 0:
                num = num / 2
                collatz_length += 1
            else:
                num = 3 * num + 1
                collatz_length += 1
        return collatz_length


    num = 1
    for i in range(5 * 10 ** 5, 10 ** 6):
        if Collatz_sequence_lenght(i) > Collatz_sequence_lenght(num):
            num = i
    print(num, Collatz_sequence_lenght(num))



except TypeError:
    print("You did not insert a valid number...")
    sys.exit()
except UnboundLocalError:
    print("You did not insert a valid number...")
    sys.exit()

print("--- %s seconds ---" % (time.time() - start_time))