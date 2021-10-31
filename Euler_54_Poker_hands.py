import string
import time


def main():

    start_time = time.time()

    filename = "Poker_hands.txt"
    file = open(filename, "r")
    text = file.read()
    poker_hands = [word.strip(string.punctuation) for word in text.split()]
    final_poker_hands = [x for x in range(1, 2001)]
    setter = 0
    for i in range(0, 2000):
        if i != 0:
            setter = i * 5
            final_poker_hands[i] = [poker_hands[setter], poker_hands[setter + 1], poker_hands[setter + 2],
                                    poker_hands[setter + 3], poker_hands[setter + 4]]
        else:
            final_poker_hands[i] = [poker_hands[setter], poker_hands[setter + 1], poker_hands[setter + 2],
                                    poker_hands[setter + 3], poker_hands[setter + 4]]


    def hand_rank(hand):
        number = [0, 0, 0, 0, 0]
        color = [0, 0, 0, 0, 0]
        for i in range(0, 5):
            number[i] = hand[i][0]
            color[i] = hand[i][1]
        translated_number_1 = [1, 1, 1, 1, 1]
        for i in range(0, 5):
            if number[i] == "A":
                translated_number_1[i] = 14
            elif number[i] == "K":
                translated_number_1[i] = 13
            elif number[i] == "Q":
                translated_number_1[i] = 12
            elif number[i] == "J":
                translated_number_1[i] = 11
            elif number[i] == "T":
                translated_number_1[i] = 10
            elif number[i] == "9":
                translated_number_1[i] = 9
            elif number[i] == "8":
                translated_number_1[i] = 8
            elif number[i] == "7":
                translated_number_1[i] = 7
            elif number[i] == "6":
                translated_number_1[i] = 6
            elif number[i] == "5":
                translated_number_1[i] = 5
            elif number[i] == "4":
                translated_number_1[i] = 4
            elif number[i] == "3":
                translated_number_1[i] = 3
            else:
                translated_number_1[i] = 2

        translated_number = list(map(int, translated_number_1))

        for i in range(4, 0, -1):
            for j in range(i):
                if translated_number[j + 1] > translated_number[j]:
                    replacer = translated_number[j]
                    translated_number[j] = translated_number[j + 1]
                    translated_number[j + 1] = replacer


        rank = -1
        if (translated_number[0] == translated_number[1] and translated_number[1] == translated_number[2] and
            translated_number[3] == translated_number[4]):
            rank = [6, translated_number[0], 0, 0, 0, 0]
            # print("You got a full of", translated_number[0], "with", translated_number[3])
        elif (translated_number[0] == translated_number[1] and translated_number[2] == translated_number[3] and
              translated_number[3] == translated_number[4]):
            rank =[6, translated_number[2], 0, 0, 0, 0]
            #pprint("You got a full of", translated_number[3], "with", translated_number[1])
        elif (translated_number[0] == translated_number[1] and translated_number[1] == translated_number[2] and
              translated_number[2] == translated_number[3]):
            rank = [7,translated_number[0], 0, 0, 0, 0]
            #print("You got four", translated_number[0])
        elif (translated_number[1] == translated_number[2] and translated_number[2] == translated_number[3] and
              translated_number[3] == translated_number[4]):
            rank =[7, translated_number[1], 0, 0, 0, 0]
            # print("You got four", translated_number[1])
        else:
            if (color[0] == color[1]) and (color[1] == color[2]) and (color[2] == color[3]) and (color[3] == color[4]):
                if (translated_number[0] - translated_number[1] == 1) and (translated_number[1] -
                    translated_number[2] == 1) and (translated_number[2] - translated_number[3] == 1)\
                        and (translated_number[3] - translated_number[4] == 1):
                    if translated_number[0] == 14:
                        rank = [9, 0, 0, 0, 0]
                        #print("You got a ROYAL flush!!!!!!!!")
                    else:
                        rank = [8, translated_number[0], 0, 0, 0, 0]
                       # print("You got", translated_number[0], "high straight flush!")
                else:
                    rank = [5, translated_number[0], translated_number[1], translated_number[2], translated_number[3],
                            translated_number[4]]
                    #print("You got a flush!")
            else:
                if (translated_number[0] - translated_number[1] == 1) and (translated_number[1] -
                        translated_number[2] == 1) and (translated_number[2] - translated_number[3] == 1)\
                        and (translated_number[3] - translated_number[4] == 1):
                    rank = [4, translated_number[0], 0, 0, 0, 0]
                    #print("You got", translated_number[0], "high straight!")

                elif (translated_number[1] - translated_number[2] == 0 and translated_number[2] -
                      translated_number[3] == 0 ):
                    rank = [3, translated_number[1], translated_number[0], translated_number[4], 0]
                    # print("You got three of", translated_number[0])
                elif ((translated_number[0] - translated_number[1] == 0  and translated_number[1] -
                       translated_number[2] == 0)):
                    rank = [3, translated_number[0], translated_number[3], translated_number[4], 0]
                    # print("You got three of", translated_number[1])
                elif (translated_number[2] - translated_number[3] == 0 and translated_number[3] -
                      translated_number[4] == 0):
                    rank = [3, translated_number[2], translated_number[0] ,translated_number[1], 0]
                    # print("You got three of", translated_number[2])
                elif (translated_number[0] - translated_number[1] == 0 and translated_number[2] -
                      translated_number[3] == 0):
                    rank = [2, translated_number[0], translated_number[2], translated_number[4], 0]
                    # print("You got", translated_number[0], "with", translated_number[2])
                elif (translated_number[1] - translated_number[2] == 0 and translated_number[3] -
                      translated_number[4] == 0):
                    rank = [2, translated_number[1], translated_number[3], translated_number[0], 0]
                    # print("You got", translated_number[1], "with", translated_number[3])
                elif (translated_number[0] - translated_number[1] == 0 and translated_number[3] -
                      translated_number[4] == 0):
                    rank = [2, translated_number[0], translated_number[3], translated_number[2], 0]
                    # print("You got", translated_number[0], "with", translated_number[3])
                elif (translated_number[0] - translated_number[1] == 0):
                    rank = [1, translated_number[0], translated_number[1], translated_number[2], translated_number[3],
                            translated_number[4]]
                    # print("You got a pair of", translated_number[0])
                elif (translated_number[1] - translated_number[2] == 0):
                    rank = [1, translated_number[1], translated_number[0], translated_number[2], translated_number[3],
                            translated_number[4]]
                    # print("You got a pair of", translated_number[1])
                elif (translated_number[2] - translated_number[3] == 0):
                    rank = [1, translated_number[2], translated_number[0], translated_number[1], translated_number[3],
                            translated_number[4]]
                    # print("You got a pair of", translated_number[2])
                elif (translated_number[3] - translated_number[4] == 0):
                    rank = [1, translated_number[3], translated_number[0], translated_number[1], translated_number[2],
                            translated_number[4]]
                    # print("You got a pair of", translated_number[3])
                else:
                    rank = [0, translated_number[0], translated_number[1], translated_number[2], translated_number[3],
                            translated_number[4]]
                    #print("You got a high card :(")
        """
        if rank == 9:
            print("Royal flush")
        elif rank == 8:
            print("Straight flush")
        elif rank == 7:
            print("Four of a kind")
        elif rank == 6:
            print(("Full house"))
        elif rank == 5:
            print("Flush")
        elif rank == 4:
            print("Straight")
        elif rank == 3:
            print("Three of a kind")
        elif rank == 2:
            print("Two pairs")
        elif rank == 1:
            print("One pair")
        elif rank == 0:
            print("High card")
        else:
            print("Error")
        """
        return [translated_number, rank]


    ranked_numbers = [x for x in range(0, 2000)]
    ranks = [x for x in range(0, 2000)]
    for i in range(0, 2000):
        ranked_numbers[i] = hand_rank(final_poker_hands[i])[0]
        ranks[i] = hand_rank(final_poker_hands[i])[1]
        ranked_numbers_1 = ranked_numbers[i]


    counter_winner_1 = 0
    counter_winner_2 = 0
    for i in range(0, 2000, 2):
        if ranks[i][0] > ranks[i + 1][0]:
            #print("Player one wins")
            counter_winner_1 += 1
        elif ranks[i][0] < ranks[i + 1][0]:
            #print("Player two wins")
            counter_winner_2 += 1
        else:
            if ranks[i][1] > ranks[i + 1][1]:
                #print("Player one wins")
                counter_winner_1 += 1
            elif ranks[i][1] < ranks[i + 1][1]:
                #print("Player two wins")
                counter_winner_2 += 1
            else:
                if ranks[i][2] > ranks[i + 1][2]:
                    #print("Player one wins")
                    counter_winner_1 += 1
                elif ranks[i][2] < ranks[i + 1][2]:
                    #print("Player two wins")
                    counter_winner_2 += 1
                else:
                    if ranks[i][3] > ranks[i + 1][3]:
                        #print("Player one wins")
                        counter_winner_1 += 1
                    elif ranks[i][3] < ranks[i + 1][3]:
                        #print("Player two wins")
                        counter_winner_2 += 1
                    else:
                        if ranks[i][4] > ranks[i + 1][4]:
                            #print("Player one wins")
                            counter_winner_1 += 1
                        elif ranks[i][4] < ranks[i + 1][4]:
                            #print("Player two wins")
                            counter_winner_2 += 1


    print("Number of player's one wins =", counter_winner_1)

    file.close()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()


