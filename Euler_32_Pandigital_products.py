import time


def main():
    start_time = time.time()
    def pandigital(num):
        if len(str(num)) == 9:
            if ''.join(sorted(list(str(num)))) == "123456789":
                return True
        else:
            return False

    s = 0
    i = 1
    pandigitals = set()
    while i <= 160:
        for j in range(0, 9000):
            if pandigital(str(i) + str(j) + str(i * j)):
                if not i * j in pandigitals:
                    s += i*j
                    pandigitals.add(i*j)
                    print(i, "x", j, "=", i*j)

        i += 1
    print(s)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()