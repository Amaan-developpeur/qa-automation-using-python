import pytest

@pytest.fixture
def active_user():
    return {
        "username": "amaan",
        "active": True,
        "role": "user"
    }

@pytest.fixture
def inactive_admin():
    return {
        "username": "admin",
        "active": False,
        "role": "admin"
    }
