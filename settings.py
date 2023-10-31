import os
#word list from net
#https://raw.githubusercontent.com/comp-core/Think-Python/master/words.txt


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


FILE_FOLDER = os.path.join(os.getcwd(), "files")
USER_FILE_PATH = os.path.join(FILE_FOLDER, "enregistrement.txt")
WORD_LIST_FILE_PATH = os.path.join(FILE_FOLDER, "words.txt")
SALT_PATH = os.path.join(FILE_FOLDER, "salt.pickle")
RSA_FOLDER_PATH = os.path.join(FILE_FOLDER, "RSA_keys")
RSA_CERTIFICATE_FOLDER_PATH = os.path.join(RSA_FOLDER_PATH, "certif")

create_folder(FILE_FOLDER)
create_folder(RSA_FOLDER_PATH)
create_folder(RSA_CERTIFICATE_FOLDER_PATH)

