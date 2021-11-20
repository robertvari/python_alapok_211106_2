import os, json

DATA_FILE = "phonebook.json"


def menu():
    print("="*50, "PHONEBOOK APP: MAIN MENU", "="*50)
    print("1. Print phonebook\n"
          "2. Add person\n"
          "3. Find person\n"
          "4. Exit")

    user_input = input()
    return user_input


def print_phonebook():
    phonebook = load_phonebook()
    if not phonebook:
        print("Phonebook doesn't exists. Please add a person.")
        return

    for phone, person_data in phonebook.items():
        print("="*50)
        print(f"Phone: {phone}\n"
              f"Name: {person_data['name']}\n"
              f"Address: {person_data['address']}")
        print("=" * 50)



def add_person():
    phonebook = load_phonebook()

    name = input("Name:")
    phone = input("Phone:")
    address = input("Address:")

    phonebook[phone] = {"name": name, "address": address}

    save_phonebook(phonebook)
    print("Data saved.")


def find_person():
    pass


def close_app():
    print("Have a nice day!")
    exit()


def load_phonebook():
    '''
    Returns a dictionary with phonebook data if exists.
    :return: dict
    '''

    # check if phonebook.json exists
    if not os.path.exists(DATA_FILE):
        return {}

    # read json file and return as a dictionary
    with open(DATA_FILE) as f:
        return json.load(f)


def save_phonebook(phonebook):
    with open(DATA_FILE, "w") as f:
        json.dump(phonebook, f)