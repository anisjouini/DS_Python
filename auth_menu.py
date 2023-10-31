from hash_menu import hash_menu
from crypto_menu import crypto_menu
from certif_menu import certif_menu
from colorama import Fore, Style
from pyfiglet import Figlet
f = Figlet()


def menu():
    print("1 - 🙈  Hashing")
    print("2 - ⚡  Crypting RSA")
    print("3 - 📜  Certificate RSA")
    print("4 - 👈  Log out")


def auth_menu():
    print(Fore.CYAN + f.renderText('Menu'))
    print(Style.RESET_ALL)
    while True:
        try:
            menu()
            choice = int(input("⛏️   => "))
            match choice:
                case 1:
                    hash_menu()
                case 2:
                    crypto_menu()
                case 3:
                    certif_menu()
                case 4:
                    break
                case _:
                    print(Fore.LIGHTYELLOW_EX +
                          "wrong choice , 🤓 please wear your glasses")
                    print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "something went wrong 😮 please try again")
            print(Style.RESET_ALL)
