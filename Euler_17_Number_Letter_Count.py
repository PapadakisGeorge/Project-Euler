import time



start_time = time.time()
dict_1_to_9 = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        }
dict_10_to_19 = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        }
lst_1 = [len(dict_1_to_9[i]) for i in dict_1_to_9]
lst_2 = [len(dict_10_to_19[i]) for i in dict_10_to_19]

letter_count_1_to_9 = 0
letter_count_10_to_19 = 0
for i in range(0, len(lst_1)):
    letter_count_1_to_9 += lst_1[i]
for i in range(0, len(lst_2)):
    letter_count_10_to_19 += lst_2[i]
print(letter_count_1_to_9)
print(letter_count_10_to_19)
letter_count_20_to_99 = 8 * letter_count_1_to_9 + 10 * (len("twenty") + len("thirty")+
                                                                               len("forty") + len("fifty") +
                                                                               len("sixty") + len("seventy") +
                                                                            len("eighty") + len("ninety"))
letter_count_1_to_99 = letter_count_1_to_9 + letter_count_10_to_19 + letter_count_20_to_99
print(letter_count_1_to_99)
letter_count_100_to_999 = 100 * letter_count_1_to_9 + 9 * letter_count_1_to_99 + 9 * len("hundred") + 891 *\
                          (len("hundred") + len("and"))
print(letter_count_100_to_999)
letter_count = letter_count_1_to_99 + letter_count_100_to_999 + len("one") + len("thousand")
print(letter_count)





print("--- %s seconds ---" % (time.time() - start_time))