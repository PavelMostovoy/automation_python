def func(var_a, var_b):
    return var_a + var_b


test_data = {1: (2, 3), 4: (1, 3), "ab": ("a", "b"), "df": ("f", "d"),
             "fail": (1, "a")}

errors = []

for key, value in test_data.items():
    try:
        assert key == func(*value), f"test fails with {key} , {value}"
    except Exception as error:
        errors.append(error)

assert not errors, print(errors)

print("runing")