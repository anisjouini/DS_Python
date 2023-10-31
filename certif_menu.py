
from Certificate import Certificate
from settings import RSA_CERTIFICATE_FOLDER_PATH
from colorama import Fore, Style


def menu():
    print("1 - 🚀  Generate RSA KEYS")
    print("2 - ⚙️   Generate certificate")
    print("3 - 🔐  Encrypt message")
    print("4 - 🚧  return to menu")


def certif_menu():
    certif_object = Certificate()
    while True:
        try:
            menu()
            choice = int(input("⛏️   => "))
            match choice:
                case 1:
                    certif_object.gen_keys(RSA_CERTIFICATE_FOLDER_PATH)
                    print(
                        Fore.GREEN + f"KEYS 🗝️  generated in {RSA_CERTIFICATE_FOLDER_PATH}")
                    print(Style.RESET_ALL)

                case 2:
                    certif_object.gen_certif(RSA_CERTIFICATE_FOLDER_PATH)
                    print(
                        Fore.GREEN + f"Certificate 📑  generated in {RSA_CERTIFICATE_FOLDER_PATH}")
                    print(Style.RESET_ALL)

                case 3:
                    message = input("message to encrypt 💬 => ")
                    encrypted_message = certif_object.encrypt(message)
                    print(Fore.LIGHTCYAN_EX +
                          "Encrypted to  🤖 : " + encrypted_message)
                    print(Style.RESET_ALL)
                case 4:
                    break
                case _:
                    print(Fore.LIGHTYELLOW_EX +
                          "wrong choice , 🤓 please wear your glasses")
                    print(Style.RESET_ALL)
        except Exception as e:
            print(e)
            print(Fore.RED + "something went wrong 😮 please try again")
            print(Style.RESET_ALL)
