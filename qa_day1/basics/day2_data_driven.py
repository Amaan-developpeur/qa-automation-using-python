def can_user_login(attempts, locked):
    if locked:
        return False
    if attempts <= 0:
        return False
    return True

def test_single_case():
    result = can_user_login(3,False)
    assert result is True
    # If Nothing Prints Pass
    # Silence is Success in Automation

# Multiple Test Cases
test_cases = {
    # "CaseNumber": [attempts, locked, expected]
    "case1": [5, False, True],
    "case2": [6, True, False],
    "case3": [-1, False, False],
    "case4": [0, False, False],
    "case5": [10, False, True],
    "case6": [0, True, False],
    "case7": [-1, True, False],
    "case8": [10,False, True],
}
def test_multiple_cases(test_cases):
    for case in test_cases.values():
        result = can_user_login(case[0], case[1])
        assert result == case[2]

test_multiple_cases(test_cases)

api_responses = [
    {"status": 200, "user": "admin", "active": True},
    {"status": 403, "user": "guest", "active": False},
    {"status": 500, "user": "admin", "active": False},
]
def test_api_responses(api_responses):
    for response in api_responses:
        assert "status" in response
        assert "user" in response
        assert "active" in response

        if response["status"] == 200:
            assert response["active"] is True
        else:
            assert response["active"] is False

def test_api_responses2(api_responses):
    for i, response in enumerate(api_responses):
        assert "status" in response, f"[Case {i}] Missing 'status'"
        assert "user" in response, f"[Case {i}] Missing 'user'"
        assert "active" in response, f"[Case {i}] Missing 'active' key → {response}"

        if response["status"] == 200:
            assert response["active"] is True
        else:
            assert response["active"] is False


test_api_responses2(api_responses)

passed = 0
failed = 0

for x in test_cases.values():
    result = can_user_login(x[0], x[1])
    if result == x[2]:
        passed += 1
    else:
        failed += 1

print(f"Passed: {passed}, Failed: {failed}")
