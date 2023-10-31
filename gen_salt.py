import bcrypt
import pickle
from settings import SALT_PATH
import os

def generate_salt():
    return bcrypt.gensalt().decode()


def load_salt_from_file():
    with open(SALT_PATH, "rb") as f:
        salt_data = pickle.load(f)
    f.close()
    return salt_data


def save_salt_to_file():
    with open(SALT_PATH, "wb") as f:
        pickle.dump(generate_salt(), f)
    f.close()


def get_salt():
    if not os.path.exists(SALT_PATH):
        save_salt_to_file()
    return load_salt_from_file()
