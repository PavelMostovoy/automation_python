import pytest
from hidden import our_func


# def test_funct_2():
#     assert our_func(5, 6, 2) == 12
#
#
# def test_funct_3():
#     assert our_func(5, 5, 2) == 2

test_data = [(10, 5, 3, 8),
             (5, 6, 2, 13),
             (5, 5, 2, 2),
             (100, 1200, 0, 300),
             (10, 5, 3, 8),
             (5, 6, 2, 13),
             (5, 5, 2, 2),
             (100, 1200, 0, 300)
             ]

@pytest.mark.smoke
@pytest.mark.parametrize("value, value_1, value_2, result", test_data)
def test_funct_0(value,value_1, value_2, result):
    # print(value, value_1, value_2, result)
    assert our_func(value, value_1, value_2) == result
