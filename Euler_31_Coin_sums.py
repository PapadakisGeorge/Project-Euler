import time

def main():
    start_time = time.time()

    def diophantine_count(a, n):
        def p(a, m, j):
            if j == 0:
                return int(m == 0)
            else:
                return sum([p(a[1:], m - k * a[0], j - 1)
                            for k in range(1 + m // a[0])])

        return p(a, n, len(a))

    print(diophantine_count([1, 2, 5, 10, 20, 50, 100, 200], 200))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()