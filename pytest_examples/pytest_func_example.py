import pytest


def setup():
    print("basic setup into module")


def teardown():
    print("basic teardown into module")


# def setup_module(module):
#     print("module setup")
#
#
# def teardown_module(module):
#     print("module teardown")
#

def setup_function(function):
    print("function setup")


def teardown_function(function):
    print("function teardown")


@pytest.mark.smoke
@pytest.mark.parametrize()
def test_numbers_3_4():
    print("test 3*4")
    pytest.data = 345
    assert 3 * 4 == 12


@pytest.mark.smoke
@pytest.mark.slow
def test_strings_a_3():
    local_data = pytest.data
    print("test a*3")
    assert local_data == 345
    # assert 'a' * 3 == 'aaaa'
