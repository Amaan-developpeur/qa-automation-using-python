# ----------------------------------------------------

# Fixtures are used when multiple tests require same data to perform different tests
# Fictures is a function that provides something[data] a test needs before ot runs.

# -----------------------------------------------
import pytest 

def final_price(price, discount):
    return price - (price*discount)

@pytest.fixture
def discount():
    return 0.10

# Different commodities have different prices
# But, same discount
@pytest.mark.parametrize(
    "price,expected",
    [
        (1000,900),
        (1200,1080)
    ]
)
def test_final_price(price,expected,discount):
    assert final_price(price, discount) == expected

# discount is a function and we are not using ()
# Because pytest understands that it is a ficture
# And prepares the data for it before running the test
# Pytest Calls them and injects their retured values into tests.

# -----------------------------------------------------

@pytest.fixture
def active_user():
    return {
        "username": "amaan",
        "active": True,
        "role": "user"
    }


def test_user_is_active(active_user):
    assert active_user["active"] is True

# -----------------------------------------------
def test_user_has_username(active_user):
    assert active_user["username"] == "amaan"

def test_user_has_role(active_user):
    assert active_user["role"] == "user"

def can_login(user):
    if not user["active"]:
        return False
    return True


def test_active_user_can_login(active_user):
    assert can_login(active_user) is True
# -------------------------------------------------

# In a fixture, yield splits the function in 2 parts. 
# Before yield ---> SETUP
# After yield ---> TEARDOWN

# Because, sometimes something must be created before the test
# And destroyed after the test
# Ex: Database Connection

import os

@pytest.fixture
def temp_file():
    with open("data.txt", "w") as fp:
        fp.write("hello")
    yield "data.txt"
    os.remove("data.txt")

def test_temp_file(temp_file):
    with open(temp_file, "r") as fp:
        content = fp.read()
        assert content == "hello"

# ----------------------------------------------

def add(a,b):
    return a+b

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10,10,20),
        (20,30,50),
        (5,5,10)
    ]
)
def test_add(a,b,expected):
    assert add(a,b) == expected






