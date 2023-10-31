import os
from gen_salt import get_salt
import bcrypt
import time
from User import User
from settings import USER_FILE_PATH

def hash_password(passwd: str) -> str:
    salt: str = get_salt()
    return bcrypt.hashpw(passwd.encode(), salt.encode()).decode()


def check_password(passwd: str, hashed_pwd: str) -> bool:
    return bcrypt.checkpw(passwd.encode(), hashed_pwd.encode())


def retrive_users():
    try:
        if not os.path.exists(USER_FILE_PATH):
            return []
        users_list = []
        with open(USER_FILE_PATH, "r") as f:
            for line in f:
                user_data = line.split("\t")
                users_list.append(User.fromdict({
                    'email': user_data[0],
                    'password': user_data[1],
                    'timestamp': user_data[2]
                }))
        f.close()
        return users_list
    except Exception as e:
        print(str(e))
        return None


def save_to_file(email: str, password: str) -> bool:
    try:
        with open(USER_FILE_PATH, "+a") as f:
            f.write(f"{email}\t{hash_password(password)}\t{time.time()}\n")
        f.close()
        return True
    except Exception as e:
        return False


def search_by_email(email: str) -> dict | bool:
    try:
        users: list = retrive_users()
        for user in users:
            if email == user.email:
                return user
        return False
    except Exception as e:
        return False
