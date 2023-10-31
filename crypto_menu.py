
from RSA import RSAClass
from settings import RSA_FOLDER_PATH
from colorama import Fore, Style
from pyfiglet import Figlet
f = Figlet()


def menu():
    print("1 - 🚀  Gen Keys")
    print("2 - 🔐  Encrypt message using RSA ")
    print("3 - 😈  Decrypt message")
    print("4 - ✍️   Create signature on a message")
    print("5 - 👀  Verify signature on a message")
    print("6 - 🚧  return to menu")


def crypto_menu():
    print(Fore.LIGHTBLUE_EX + f.renderText('Crypto'))
    print(Style.RESET_ALL)
    rsa_object = RSAClass()
    last_encryption = None
    last_sig = None
    while True:
        try:
            menu()
            choice = int(input("⛏️   => "))
            match choice:
                case 1:
                    rsa_object.gen_keys(RSA_FOLDER_PATH)
                    print(Fore.LIGHTGREEN_EX +
                          f"keys 🗝️  generated in {RSA_FOLDER_PATH}")
                    print(Style.RESET_ALL)
                case 2:
                    message = input("Message to encrypt 💬  -> ")
                    msg_encrypt = rsa_object.encrypt(message)
                    last_encryption = msg_encrypt
                    print(f"Message  💬 : {message}")
                    print(Fore.LIGHTCYAN_EX +
                          f"Encrypted to  🤖  : {msg_encrypt}")
                    print(Style.RESET_ALL)

                case 3:
                    encrypted_message = input(
                        "Encrypted message to decrypt 🙄  -> ")
                    if encrypted_message == "":
                        encrypted_message = last_encryption
                        print(" 📢  using last encrypted message")
                    try:
                        msg_decrypt = rsa_object.decrypt(encrypted_message)
                        print(Fore.LIGHTYELLOW_EX +
                              f"Encrypted Message  💬 : {encrypted_message}")
                        print(Fore.GREEN +
                              f"Decrypted to  🤖 : {msg_decrypt.decode()}")
                        print(Style.RESET_ALL)
                    except Exception as e:
                        print(Fore.RED +
                              f"Decrypting failed  ❌")
                        print(Style.RESET_ALL)

                case 4:
                    word = input("💬   ->")
                    last_sig = rsa_object.create_sig(word)
                    print(Fore.LIGHTBLUE_EX +f"Signature : {last_sig}")
                    print(Style.RESET_ALL)
                case 5:
                    signature = input("signature ⚠️  -> ")
                    if signature == "":
                        print("📢  Using last signature")
                        signature = last_sig
                    word = input("Word  💬 ->")
                    if rsa_object.verify_sig(word, signature):
                        print(Fore.GREEN + "Signature verified 👍")
                        print(Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Signature failed 👎")
                        print(Style.RESET_ALL)
                case 6:
                    break
                case _:
                    print(Fore.LIGHTYELLOW_EX +
                          "wrong choice , 🤓  please wear your glasses")
                    print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "something went wrong 😮  please try again")
            print(Style.RESET_ALL)
