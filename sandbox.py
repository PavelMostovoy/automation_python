from pytest_examples.hidden import our_func

'''
case 1 : a = 10 b = 5 c = 3  => 8
case 2 : a = 5 b = 6 c = 2 => 13
case 3 : a = b = 5 c = 2 => 12
case 4 : a = 100, b = 200, c = 0 , =>300  
'''
errors = []

test_data = [(10, 5, 3, 8),
             (5, 6, 2, 13),
             (5, 5, 2, 2),
             (100, 1200, 0, 300),
             (10, 5, 3, 8),
             (5, 6, 2, 13),
             (5, 5, 2, 2),
             (100, 1200, 0, 300)]

for data in test_data:
    a, b, c, r = data[:]
    try:
        assert our_func(a, b, c) == data[
            -1], f"Function works incorrectly with data {a=}, " \
                 f"{b=}," \
                 f"{c=} return {r=}"
    except AssertionError as e:
        errors.append(e)

assert not errors, f"f errors are : {errors}"
