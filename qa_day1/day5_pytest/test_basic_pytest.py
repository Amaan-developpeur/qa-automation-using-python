def test_simple_math():
    assert 2 + 2 == 4

# --------------------------------

def divide_numbers(a, b):
    return a / b

def test_divide_normal():
    assert divide_numbers(10, 2) == 5

# No manual calls required
# pytest handles everything

# ---------------------------------------------
import pytest

# This comes under the Negative Testing aspect.
# It’s about making sure it breaks when it should — cleanly, intentionally, and without lying.
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

# -----------------------------------

@pytest.mark.parametrize(
    "a,b,expected",
    # Pytest reads this once, then runs the test multiple times, injecting different values each run.
    # Pytest parses this string, splits it by commas, strips whitespace, and maps the names to function arguments.
    # Run 1 → a=10, b=2, expected=5
    # Run 2 → a=20, b=4, expected=5
    # Run 3 → a=9,  b=3, expected=3

    [
        (10,5,2),
        (20,4,5),
        (9,3,3)

    ]
)
def test_divide_multiple(a,b,expected):
    assert divide_numbers(a,b) == expected

# pytest -v (--verbose)
# Runs the same tests
# Shows each test name explicitly
# Displays full test node paths

#------------------------------------------
@pytest.mark.parametrize(
    "a,b",
    [
        (10, 0),
        ("10", 2),
        (None, 1),
    ]
)
def test_divide_invalid_inputs(a, b):
    with pytest.raises(Exception):
        divide_numbers(a, b)
#-----------------------------------------
# pytest -x stops execution on the first failure.
# While it’s useful locally for fast debugging, it’s dangerous in CI because it hides additional failures, masks flaky tests, 
# and gives a false sense of system health.
# Making us feel that it was only 1 failure, where in reality there could
# be many more.


#---------------------
# pytest --maxfail=n
# Allows atmost n number of failures
# And then stops execution

#--------------------------------------

