import time


def main():
    start_time = time.time()

    def powers(a, b):
        powers = set()
        for i in range(2, a + 1):
            for j in range(2, b + 1):
                powers.add(i ** j)
        return powers
    print(len(powers(100, 100)))







    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()