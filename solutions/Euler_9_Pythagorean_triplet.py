from utils import Timer


# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

@Timer.timeit
def main():
    def pythagorean_triplets_with_limitation(limits, limitation):
        for i in range(1, limits):
            for j in range(i, limits):
                for k in range(j, limits):
                    if i + j + k == limitation:
                        if i ** 2 + j ** 2 == k ** 2:
                            return i * j * k

    print(pythagorean_triplets_with_limitation(1000, 1000))


if __name__ == '__main__':
    main()
