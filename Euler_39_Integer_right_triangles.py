from utils import Timer
from collections import Counter

@Timer.timeit
def main():

    def find_triple(upper_boundary=1000):
        for c in range(5, upper_boundary + 1):
            for b in range(4, c):
                for a in range(3, b):
                    if a * a + b * b == c * c:
                        yield a, b, c
    per = []
    triplets = list(find_triple(upper_boundary=1000))
    for trip in triplets:
        per.append(trip[0]+trip[1]+trip[2])
    print(Counter(per))



if __name__ == '__main__':
    main()

