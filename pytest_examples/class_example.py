import requests
import pytest

from hidden import our_func


def save_data(data):
    with open("log.txt", "a") as f:
        f.write(data)


class TestSuite:

    def setup_class(self):
        from hidden import test_data
        local_variable  = test_data
        print("Tests suite started")

    def teardown_class(self):
        print("Tests Suite  done")

    def setup(self):
        print("single test started")

    def teardown(self):
        print("singlle test finished")

    def test_first_check(self):
        print("inside test")
        assert our_func(1, 2, 3) != 3

    def test_second_check(self):
        print("inside test")
        assert our_func(5, 6, 2) == 12

    def test_third_check(self):
        print("inside test")
        assert our_func(5, 5, 2) == 2

    def test_forth_check(self):
        print("inside test")
        assert our_func(1, 2, 3) == 6
