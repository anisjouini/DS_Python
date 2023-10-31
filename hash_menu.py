import hashlib
import bcrypt
from progress.bar import Bar
from settings import WORD_LIST_FILE_PATH
import time
from pyfiglet import Figlet
from colorama import Fore, Style
f = Figlet()


def menu():
    print("1 - 🤫 hash password using SHA256")
    print("2 - 🤐 hash password using BCRYPT")
    print("3 - ☠️  attack by dictionary")
    print("4 - 🚧 return to menu")


def hash_256(password: str):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    print(Fore.LIGHTCYAN_EX + f"hashed password ☢️ : {hashed}")
    print(Style.RESET_ALL)
    return hashed


def hash_with_salt(password: str):
    salt = bcrypt.gensalt()
    print('using salt 🧂  : '+salt.decode())
    hashed = bcrypt.hashpw(password.encode(), salt).decode()
    print(Fore.GREEN + f"hashed password ☢️  : {hashed}")
    print(Style.RESET_ALL)
    return hashed


def dict_attack(password: str):
    try:
        start = time.time()
        hashed_word = hash_256(password.strip())
        f = open(WORD_LIST_FILE_PATH, 'r')
        data = f.readlines()
        with Bar('Processing  ☣️ ', max=len(data)) as bar:
            count = 1
            for line in data:
                bar.next()
                if hashed_word == hashlib.sha256(line.strip().encode()).hexdigest():
                    print("\n")
                    print(Fore.RED+"founded 😒 , please consider to change the password")
                    print(
                        Fore.YELLOW+f"founded after {count} iterations in {time.time()-start} , so easy 🤣 ")
                    print(Style.RESET_ALL)

                    f.close()
                    return True
                count += 1
            print("\n")
            print(Fore.GREEN + "password not found 😀")
            print(Style.RESET_ALL)
            f.close()
            return False
    except Exception as e:
        print("file not found")


def hash_menu():
    print(Fore.LIGHTBLUE_EX + f.renderText('Hashing'))
    print(Style.RESET_ALL)
    while True:
        try:
            menu()
            choice = int(input("⛏️   => "))

            match choice:
                case 1:
                    password = input("password to hash 🔏  -> ")
                    hash_256(password)
                case 2:
                    password = input("password to hash 🔏  -> ")
                    hash_with_salt(password)
                case 3:
                    print(Fore.LIGHTRED_EX + f.renderText('dict attack'))
                    print(Style.RESET_ALL)
                    password = input("password to hash 🔏  -> ")
                    dict_attack(password)
                case 4:
                    break
                case _:
                    print(Fore.LIGHTYELLOW_EX +
                          "wrong choice , 🤓 please wear your glasses")
                    print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "something went wrong 😮 please try again")
            print(Style.RESET_ALL)
