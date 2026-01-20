# Simulates API Response, DB Record and Backend Object
def create_user(username, active=True):
    return {
        "username": username,
        "active": active,
        "role": "user"
    }

# Bad Practise + Illogical Test
def test_user_is_active_illogical():
    user = {
        "username": "amaan",
        "active": True,
        "role": "user"
    }
    assert user["active"] is True
# What this test is doing wrong

# Not calling the SUT (System Under Test)
# You defined create_user() earlier — and ignored it.

# Testing test data instead of system behavior
# You created the object inside the test and then asserted it.

# False sense of coverage
# This test will pass forever, even if create_user() is deleted or broken.

# --------------------------------------------------------------------
# A Test that does not touch the SUT[System Under Test] is not a Test.
# A Test that does not touch the SUT[System Under Test] is not a Test.
# A Test that does not touch the SUT[System Under Test] is not a Test.4
# ---------------------------------------------------------------------


# The test actually protects behavior
def test_user_is_active():
    user = create_user("amaan") # user comes from the system
    assert user["active"] is True # If create_user() breaks → test fails


test_user_is_active()
#---------------------------------------------
# Adding More Tests

def check_username_condition(username):
    if not isinstance(username, str):
        return False
    if len(username) < 5:
        return False
    if not username.isalpha():
        return False
    return True


def test_user_has_valid_username():
    user = create_user("amaan")
    result = check_username_condition(user["username"])
    assert result is True

test_user_has_valid_username()

#--Test User Has Role

def test_user_has_role():
    user = create_user("amaan")
    assert user["role"] == "user"

test_user_has_role()

#-------------------------------------------------------
def setup_active_admin():
    user = create_user("admin", active=True)
    user["role"] = "admin"
    return user

def test_admin_is_active():
    user = setup_active_admin()
    assert user["active"] is True

test_admin_is_active()

def test_admin_role():
    user = setup_active_admin()
    assert user["role"] == "admin"

test_admin_role()

# ------------------------------------

def teardown_user(user):
    user.clear()

def test_teardown_clears_user():
    user = create_user(username="amaan")
    teardown_user(user)
    assert user == {}

test_teardown_clears_user()






