b = 1

c = 2

a = b + c


def f_name():
    return b + c


def a_name():
    return b + c + a

var = lambda x : x()


print(var(f_name))

print(var(a_name))