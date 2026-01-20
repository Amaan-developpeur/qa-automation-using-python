def divide_numbers(a,b):
    return a/b 

def test_normal():
    result = divide_numbers(10,2)
    assert result == 5

test_normal()

# def test_divide_by_zero():
#     result = divide_two_numbers(10, 0)
#     assert result == 0
# Because we can't do 10/0, and we get ZeroDivisionError.
# assert result == 0, this test expectation itself is wrong

# test_divide_by_zero()

def test_divide_by_zero():
    try:
        divide_numbers(10, 0)
        assert False, "Expected ZeroDivisionError but none occurred"
    except ZeroDivisionError:
        assert True

test_divide_by_zero()

def test_invalid_type_error():
    try:
        divide_numbers("10", 2)
        assert False, "Expected Type Error"
    except TypeError:
        assert True

test_invalid_type_error()

invalid_cases = {
    "case1":["10", 2],
    "case2":[10, "2"],
    "case3":[None, 1],
    "case4":[[], 2],
}

def test_invalid_inputs():
    for x in invalid_cases.values():
        try:
            divide_numbers(x[0], x[1])
            assert False, f"Expected failure for inputs: {x[0]}, {x[1]}"
        except (TypeError, ZeroDivisionError):
            assert True

test_invalid_inputs()

def divide_numbers_bug_func(a, b):
    if b == 0:
        return 0
    return a / b

# def test_divide_numbers_bug_func():
#     result = divide_numbers_bug_func(5,0)
#     assert result == 0, f"Expected TypeError for inputs: {a}, {b}"

# test_divide_numbers_bug_func()

def test_divide_numbers_bug_func():
    try:
        divide_numbers_bug_func(5, 0)
        assert False, "Bug: divide by zero should not return 0"
    except ZeroDivisionError:
        assert True

test_divide_numbers_bug_func()




