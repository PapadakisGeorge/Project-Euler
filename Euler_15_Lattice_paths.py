import time
import math

start_time = time.time()

routes = int(math.factorial(40) / math.factorial(20)**2)
print(routes)

print("--- %s seconds ---" % (time.time() - start_time))