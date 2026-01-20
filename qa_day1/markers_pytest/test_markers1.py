import pytest

def simple_math(a,b):
    return a+b

def divide_numbers(a,b):
    return a/b

# ------------------------------------------------------------
# Smoke tests should be few
# Regression could be many
# If everything is smoke nothing is smoke
# The below tests are not following strict decipline because
# they are not testing a real system

# It is onlt for learning purpose
@pytest.mark.regression 
def test_simple_math():
    assert 2 + 2 == 4

@pytest.mark.smoke
def test_divide_normal():
    assert divide_numbers(10, 2) == 5


@pytest.mark.regression
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10,5,2),
        (20,4,5),
        (9,3,3)
    ]
)
def test_divide_multiple(a, b, expected):
    assert divide_numbers(a, b) == expected

# Negative tests belong in regression, not smoke.
@pytest.mark.regression
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

@pytest.mark.smoke
@pytest.mark.regression
def test_divide_normal():
    assert divide_numbers(10, 2) == 5





