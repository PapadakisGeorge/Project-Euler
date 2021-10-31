import time


start_time = time.time()

filename = "Names.txt"
file = open(filename, "r")
text = file.read().split(",")
names = list(sorted(text))


def letter_count(name):
    count = 0
    for i in range(1, len(name) - 1):
        count += ord(name[i]) - 64
    return count


score = 0
for i in range(0, len(names)):
    score += letter_count(names[i]) * (i + 1)
print(score)

file.close()
print("--- %s seconds ---" % (time.time() - start_time))