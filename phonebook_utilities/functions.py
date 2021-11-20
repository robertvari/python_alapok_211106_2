import os, json

DATA_FILE = "phonebook.json"


def menu():
    print("="*50, "PHONEBOOK APP: MAIN MENU", "="*50)
    print("1. List phonebook\n"
          "2. Add person\n"
          "3. Find person\n"
          "4. Exit")

    user_input = input()
    return user_input


def list_phonebook():
    pass


def add_person():
    pass


def find_person():
    pass


def close_app():
    print("Have a nice day!")
    exit()


def load_phonebook():
    '''
    Returns a dictionary with phonebook data if exists. Else returns None
    :return: dict/None
    '''

    # check if phonebook.json exists
    if not os.path.exists(DATA_FILE):
        return

    # read json file and return as a dictionary
    with open(DATA_FILE) as f:
        return json.load(f)


def save_phonebook():
    pass