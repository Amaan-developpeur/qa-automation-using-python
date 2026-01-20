def test_active_user_can_login(active_user):
    assert active_user["active"] is True
