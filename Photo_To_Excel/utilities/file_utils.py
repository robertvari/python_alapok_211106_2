import os


def get_folder_path():
    user_response = input("Photo folder:")
    while not os.path.exists(user_response):
        print(f"Folder does not exists: {user_response}")
        user_response = input("Photo folder:")

    return user_response


if __name__ == '__main__':
    get_folder_path()