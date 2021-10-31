from utils import Timer


# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

@Timer.timeit
def main():
    def sum_of_multiples(multiples, limit):
        current_sum = 0
        for candidate in range(1, limit):
            for multiple in multiples:
                if candidate % multiple == 0:
                    current_sum += candidate
                    break
        return current_sum

    print('Sum of multiples of 3 or 5 is: ', sum_of_multiples([3, 5], 1000))


if __name__ == '__main__':
    main()
