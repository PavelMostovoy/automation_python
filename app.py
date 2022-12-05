import string

import requests as requests

data = [y for y in string.ascii_lowercase + string.ascii_uppercase + string.printable + "adsewaaaasdwwaaffvfvesaa" ]

# print(data)
#
# print(data.count("a"))

def get_data(var:str):
    new_data = []
    for i in range(len(data)):
        if data[i] == var:
            new_data.append(data[i])
    return new_data

def comp(actual:str, expected = "d"):
    return actual == expected

def comp_o(actual:str, expected = "a"):
    return actual == expected

#
# new_data = get_data("a")
# print(new_data)
#
# new_data_0 = get_data("d")
#
# print(new_data_0)

newest_data = filter(comp, data)

newest_data_0 = filter(lambda x: x=="6", data)

print(list(newest_data))

print(list(newest_data_0))

data =  ["https://google.com", "https://wikipedia.com", "http://Nasa.gov"]

def our_funct(url):
    data = requests.get(url)
    return data

old_data = map(our_funct, data)

print(next(old_data))

print(next(old_data).text)

print(next(old_data))
