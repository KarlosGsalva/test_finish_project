import pytest


@pytest.fixture()
def set_up():
    print("start test")
    yield
    print("finish test")


@pytest.fixture(scope="module")
def set_group():
    print("enter system")
    yield
    print("exit system")
