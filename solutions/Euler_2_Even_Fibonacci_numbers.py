from utils import Timer, Fibonacci


# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

@Timer.timeit
def main():
    def sum_of_even_valued_fibonacci_terms(first_seed, second_seed, limit):
        current_sum = 0
        current_index = 1
        current_fibonacci = first_seed
        while current_fibonacci < limit:
            current_fibonacci = Fibonacci.generate_fibonacci_number(first_seed, second_seed, current_index)
            if current_fibonacci % 2 == 0:
                current_sum += current_fibonacci
            current_index += 1
        return current_sum

    print('Sum of even valued fibonacci terms  whose values do not exceed four million is:',
          sum_of_even_valued_fibonacci_terms(1, 2, 4000000))


if __name__ == '__main__':
    main()
