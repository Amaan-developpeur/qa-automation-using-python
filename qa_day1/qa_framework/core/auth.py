def can_login(user):
    return user.get("active", False)
