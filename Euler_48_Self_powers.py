from utils import Timer


@Timer.timeit
def main():

    def self_power(num):
        s = 0
        for i in range(1, num + 1):
            s += i ** i
        return str(s)
    print(self_power(1000)[-10:])


if __name__ == '__main__':
    main()

