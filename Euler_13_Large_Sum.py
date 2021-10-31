import time
import sys

try:
    start_time = time.time()

    filename = "50_digits_number.txt"
    file = open(filename, "r")
    text = file.read()
    numbers = list(map(int, text.split()))
    sum = 0
    for i in numbers:
        sum += i
    str_sum = str(sum)
    print(str_sum[0:10])
    file.close()
except TypeError:
    print("You did not insert a valid number...")
    sys.exit()
except UnboundLocalError:
    print("You did not insert a valid number...")
    sys.exit()

print("--- %s seconds ---" % (time.time() - start_time))