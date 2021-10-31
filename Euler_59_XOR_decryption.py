from utils import Timer
import string
from itertools import product

"""
Decryption having only the text
def decryption(text, password):
    message = []
    for i in range(0, len(text)):
        message.append(chr(text[i] ^ password[i % 3]))
    return ''.join(message)


filename = "XOR.txt"
file = open(filename, "r")
text = file.read().strip().split(',')
text = list(map(int, text))
text_1 = []
text_2 = []
text_3 = []
for i in range(0, len(text) - 2, 3):
    text_1.append(text[i])
for j in range(1, len(text) - 1, 3):
    text_2.append(text[j])
for i in range(2, len(text), 3):
    text_3.append(text[i])


def most_common(lst):
    return max(set(lst), key=lst.count)


p = [most_common(text_1) ^ 32, most_common(text_2) ^ 32, most_common(text_3) ^ 32]
s = 0
for i in decryption(text, p):
    s += ord(i)
print(s)
file.close()
"""


@Timer.timeit
def main():
    def decryption(text, password):
        message = []
        for i in range(0, len(text)):
            message.append(chr(text[i] ^ password[i % len(password)]))
        return "".join(message)

    filename = "XOR.txt"
    file = open(filename, "r")
    text = file.read().strip().split(',')
    text = list(map(int, text))
    alphabet = list(string.ascii_lowercase)
    passwords = []
    for i in product(alphabet, repeat=3):
        temp = []
        for j in range(0, 3):
            temp.append(ord(i[j]))
        passwords.append(temp)
    for p in passwords:
        counter = 0
        for i in decryption(text, p).split(' '):
            if i == "an" or i == "the" or i == "for" or i == "are" or i == "from":
                counter += 1
        if counter > 20:
            print("".join(decryption(text, p)))
            s = 0
            for i in decryption(text, p):
                s += ord(i)
            print(s)

    file.close()


if __name__ == '__main__':
    main()

