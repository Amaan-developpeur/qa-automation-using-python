print("QA Automation Starts Here")
print("=============================")
username = "admin"
password = "secret123"
login_attempts = 3
is_locked = False

print(username)
print(password)
print(login_attempts)
print(is_locked)
print("=============================")
print(type(username))
print(type(login_attempts))
print(type(is_locked))
print("===========================")
def can_user_login(attempts, locked):
    if locked:
        return False
    elif attempts <=0:
        return False
    else:
        return True
    
a = can_user_login(5, False)
b = can_user_login(0, False)
c = can_user_login(10, True)
print(a)
print(b)
print(c)
print("==============================")
# def username_and_password():
#     username = input("Enter Username: ")

#     if username.lower() != "amaan":
#         return "Incorrect User Name"

#     for attempt in range(4):
#         password = input("Enter Password: ")

#         if password == "123":
#             return "Access Granted"
#         else:
#             print(f"Incorrect password. Attempts left: {3 - attempt}")

#     return "Too many incorrect attempts"


# call = username_and_password()
# print(call)
print("================================")
assert can_user_login(3, False) == True
assert can_user_login(0, False) == False
assert can_user_login(5, True) == False
print("All Cases Passed")
print("===============")
response = {
    "status": 200,
    "message": "success",
    "data": {
        "id": 101,
        "name": "John"
    }
}
assert response["status"] == 200
assert response["data"]["name"] == "John"
print("Data Accessed")
print("=========================")

try:
    print(response["data"]["age"])
except KeyError as e:
    print("Key missing:", e)

                
