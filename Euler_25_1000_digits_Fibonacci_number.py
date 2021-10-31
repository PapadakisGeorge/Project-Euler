import sys
import time

def main():
    start_time = time.time()
    try:
        f_1 = 1
        f_2 = 2
        f = f_1 + f_2
        index = 4
        str_f = str(f)
        while len(str_f) < 1000:
            f_1 = f_2
            f_2 = f
            f = f_1 + f_2
            index += 1
            str_f = str(f)
    except TypeError:
        print("You did not insert a valid number...")
        sys.exit()
    except UnboundLocalError:
        print("You did not insert a valid number...")
        sys.exit()
    print(index)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()