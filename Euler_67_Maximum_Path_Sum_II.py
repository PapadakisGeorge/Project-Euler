import time



start_time = time.time()

filename = "Sum_2.txt"
file = open(filename, "r")
text = file.read().split(",")
triangle = list(map(int, text.split()))


row = 99
counter = 99

for ind in range(len(triangle) - 101, -1, -1):
    if counter == 0:
        row -= 1
        counter = row
    if triangle[ind + row] < triangle[ind + row + 1]:
        triangle[ind] += triangle[ind + row + 1]

    else:
        triangle[ind] += triangle[ind + row]
    counter -= 1
print(triangle[0])














file.close()

print("--- %s seconds ---" % (time.time() - start_time))