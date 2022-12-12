def func(var_a, var_b):
    print("run")
    return var_a + var_b


def func_0(var_a, var_b):
    print("run")
    return var_a - var_b

def wrapped(fu):
    print("started")
    fu(1, 3)
    print("end")


wrapped(func)

wrapped(func_0)