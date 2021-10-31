import time


def main():
    start_time = time.time()
    def diagonal(num):
        i = 1
        s = 0
        counter = 1
        temp_counter = 0
        while i <= num ** 2:
            if temp_counter == 4:
                counter += 1
                temp_counter = 0
            s += i
            i += 2 * counter
            temp_counter += 1
        return s

    print(diagonal(1001))






    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()