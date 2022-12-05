import string
from random import choice

DATA = list(string.printable)

i_data = ["a", "b", "c"]


def custom_random(init_data):
    initial_data = init_data.copy()
    while True:
        if not initial_data:
            yield "Gen is empty"
            continue
        data = choice(initial_data)
        initial_data.remove(data)
        # print(initial_data)
        print("before return ")
        yield data
        print("after return")


gen = custom_random(i_data)
print(list(gen))
