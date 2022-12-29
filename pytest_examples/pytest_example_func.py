import pytest
import requests


# @pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def fixt():
    print("started")
    yield {"initial": []}
    print("test ended")



@pytest.fixture
def fixt_new():
    print("start test")
    yield
    print("finish test")



def test_one(fixt, fixt_new):
    response = requests.get("https://google.com")
    fixt["data"] = response.text
    assert response.status_code == 200


def test_second(fixt, fixt_new):
    print("second test")
    assert len(fixt["data"]) > 0