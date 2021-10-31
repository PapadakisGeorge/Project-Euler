def string_decomposition(string):
    parts = []
    for letter in range(0, len(string)):
        parts.append(str(string)[letter])
    return parts


def reverse(number):
    reversed_digits = string_decomposition(str(number))
    reversed_string_number = ''
    for digit in reversed(reversed_digits):
        reversed_string_number += digit
    return int(reversed_string_number)


def isPalindrome(number):
    return True if number == reverse(number) else False
