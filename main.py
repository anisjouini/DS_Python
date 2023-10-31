import utils
import validators
import maskpass
from datetime import datetime
from auth_menu import auth_menu
from pyfiglet import Figlet
from colorama import Fore, Style
import time
f = Figlet()


def menu():
    print("1 - 🖊️  register")
    print("2 - 🔐 authentification ")
    print("3 - 🔚 close")


def get_email():
    while True:
        email = input("entre your email 📧 : ")
        if not validators.email_validator(email):
            print(Fore.RED + "bummer 😒 , try again")
            print(Style.RESET_ALL)
        else:
            return email


def get_password():
    while True:
        password = maskpass.askpass("entre your password 🤫 : ")
        if not validators.passwd_validator(password):
            print(Fore.LIGHTYELLOW_EX + "so week 😩 , try again")
            print(Style.RESET_ALL)
        else:
            return password


def register():
    print(Fore.BLUE + f.renderText('Register'))
    print(Style.RESET_ALL)
    while True:
        email = get_email()
        if utils.search_by_email(email):
            print(Fore.LIGHTYELLOW_EX + "🥴 this mail already exist")
        else:
            break
    password = get_password()
    while True:
        cpasswd = maskpass.askpass("confirm your password 🤫 : ")
        if cpasswd == password:
            break
        else:
            print(Fore.RED + " 😮 did you forget it already")
            print(Style.RESET_ALL)
    utils.save_to_file(email, password)
    print(Fore.GREEN + "🥳 registration with success")
    print(Style.RESET_ALL)


def authentication():
    print(Fore.BLUE + f.renderText('authentication'))
    print(Style.RESET_ALL)
    attemps = 0
    while True:
        email = get_email()
        user = utils.search_by_email(email)
        if user == False:
            print("😕 what ?")
        else:
            break
    while attemps <= 3:
        password = maskpass.askpass("entre your password 🤫 : ")
        if utils.check_password(password, user.password):
            print(Fore.GREEN + "🎉🎉🎉 Successful authentication 🎉🎉🎉 ".upper())
            print("your acount was created at : ",
                  datetime.fromtimestamp(float(user.timestamp)))
            print(Style.RESET_ALL)
            auth_menu()
            break
        else:
            match attemps:
                case 0:
                    print(Fore.RED + "you still got it 💪💪 , try again ")
                case 1:
                    print(Fore.RED + "you still got it 💪💪 , try again ")
                case 2:
                    print(
                        Fore.RED + "You only get one shot, do not miss your chance to blow 🧑🏼, try wth caution 🚨🚨")
            attemps += 1

    if attemps > 3:
        print(Fore.RED + "😬 try again later , authentication failed ")
        print("program blocked for 1 min 🕐 ")
        time.sleep(60)
        print(Style.RESET_ALL)


if __name__ == '__main__':
    print(Fore.LIGHTBLUE_EX + f.renderText('Welcome'))
    print(Style.RESET_ALL)
    while True:
        try:
            menu()
            choice = int(input("⛏️   => "))
            match choice:
                case 1:
                    register()
                case 2:
                    authentication()
                case 3:
                    print(Fore.GREEN + "au revoir 👋")
                    print(Style.RESET_ALL)
                    break
                case _:
                    print(Fore.LIGHTYELLOW_EX +
                          "wrong choice , 🤓 please wear your glasses")
                    print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "something went wrong 😮 please try again")
            print(Style.RESET_ALL)
