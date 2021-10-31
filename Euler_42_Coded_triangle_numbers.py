from utils import Timer
import itertools


@Timer.timeit
def main():
    filename = "Words.txt"
    file = open(filename, "r")
    text = file.read()

    def letter_count(word):
        count = 0
        for i in range(1, len(word) - 1):
            count += ord(word[i]) - 64
        return count
    numbers = []
    for i in text:
        numbers.append(letter_count(i))

    def triangle_num_to(n):
        def triangle_num():
            n = 1
            while True:
                yield int(n*(n+1)/2)
                n += 1
        first_n = list(itertools.islice(triangle_num(), n))
        return first_n
    counter = 0
    for i in numbers:
        if i in triangle_num_to(i + 1):
            counter += 1
    print(counter)
    file.close()

if __name__ == '__main__':
    main()

