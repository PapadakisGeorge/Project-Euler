from utils import Timer, Palindrome


# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

@Timer.timeit
def main():
    def largest_palindrome(lower_limit, upper_limit):
        candidate = 0
        for first_multiplier in range(lower_limit, upper_limit):
            for second_multiplier in range(lower_limit, upper_limit):
                product = first_multiplier * second_multiplier
                if Palindrome.isPalindrome(product) and product > candidate:
                    candidate = product
        return candidate

    print('Largest palindrome which is a product of two 3-digit numbers is: ', largest_palindrome(100, 1000))


if __name__ == '__main__':
    main()
