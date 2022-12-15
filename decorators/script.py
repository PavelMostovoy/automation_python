
import time

def outer(fun):
    def inner(*args, **kwargs):
        print("started")
        var = fun(*args, **kwargs)
        print("ended")
        return var
    return inner

def wrapper(fun):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        var = fun(*args, **kwargs)
        print(time.perf_counter() - start_time)
        return var
    return inner

@outer
@wrapper
def funct(var):
    result = 0
    print("function run")
    for i in range(1, var + 1):
        result += var ** var
    return result


print(funct(19))

