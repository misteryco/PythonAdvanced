import os
import json
from canvas import *


curr_path = os.path.dirname(__file__)
print(f"curr_path = {curr_path}")
registration_file_path = os.path.join(curr_path, "db", "user_credentials_db.txt")
print(f"file_path = {registration_file_path}")


def login_check(u, p):
    print(f"initial login Check: username = {u}; password = {p}")
    with open(registration_file_path) as users_file:
        for line in users_file:
            line_as_dict = json.loads((line.strip()))
            if line_as_dict.get("Username") == u and line_as_dict.get("Password") == p:
                print(f"you have right user privileges to enter the shop : {u}, {p}")
                return True
            else:
                print(f"you Fucked up  : I need : {u}, {p} you give: {line_as_dict.get('Username')}, {line_as_dict.get('Password')} ")
                return False


def user_registration(l_ist):
    user_data_dict = {}
    for field in l_ist:
        user_data_dict[field[0]] = field[1]
    with open(registration_file_path, "a") as users_file:
        users_file.writelines(json.dumps(user_data_dict))
        users_file.writelines("\n")
        print(user_data_dict)
    return
