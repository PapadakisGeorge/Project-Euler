from utils import Timer



@Timer.timeit
def main():


    def number_decomposition(num):
        str_num = str(num)
        digits = []
        for i in range(0, len(str_num)):
            digits.append(int(str_num[i]))
        return digits

    def palindromic_number(num):
        digits = number_decomposition(num)
        if digits == list(reversed(digits)):
            return True
        else:
            return False


    def double_base_palindromic(num):
        if palindromic_number(num) and palindromic_number(bin(num)[2:]):
            return True
        else:
            return False

    s = 0
    for i in range(0, 10**6):
        if double_base_palindromic(i):

            s += i
    print(s)
if __name__ == '__main__':
    main()