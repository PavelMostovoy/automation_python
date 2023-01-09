import random
import time


st = time.time()
time.sleep(random.randint(1,3))
et = time.time()

print(round((et - st), 2))