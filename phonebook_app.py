from phonebook_utilities import functions


def main():
    menu_choice = functions.menu()

    if menu_choice == "4":
        functions.close_app()
    elif menu_choice == "1":
        functions.print_phonebook()
    elif menu_choice == "2":
        functions.add_person()
    elif menu_choice == "3":
        functions.find_person()
    else:
        print("Wrong number try again.")
        main()

main()