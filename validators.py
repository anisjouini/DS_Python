import re


def email_validator(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email)


def passwd_validator(passwd):
    flag = True
    if (len(passwd) <= 8):
        print("password must be at least 8 characters")
        flag = False
    elif not re.search("[a-z]", passwd):
        flag = False
    elif not re.search("[A-Z]", passwd):
        print("password must have at least 1 character uppercase")
        flag = False
    elif not re.search("[0-9]", passwd):
        print("password must have at least 1 digit")
        flag = False
    elif not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', passwd):
        print("password must have at least 1 speacial character")
        flag = False
    # elif re.search("\s", passwd):
    #     flag = -1
    return flag
