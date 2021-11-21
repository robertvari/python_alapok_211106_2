import os


def get_folder_path():
    user_response = input("Photo folder:")
    while not os.path.exists(user_response):
        print(f"Folder does not exists: {user_response}")
        user_response = input("Photo folder:")

    return user_response


def get_files(root_folder: str, files=[], name_filter=None):
    assert os.path.exists(root_folder), f"Folder does not exist: {root_folder}"

    folder_content = os.listdir(root_folder)

    # list comprehension
    all_files = [
        os.path.join(root_folder, i) for i in folder_content  # loop function
        if os.path.isfile(os.path.join(root_folder, i))  # condition
    ]

    # filter found files
    if name_filter:
        all_files = [
            i for i in all_files # loop function
            if name_filter.lower() in os.path.basename(i).lower()  # condition
        ]

    # store found files
    files += all_files

    # get all subfolders
    subfolders = [
        os.path.join(root_folder, i) for i in folder_content  # loop function
        if os.path.isdir(os.path.join(root_folder, i))  # condition
    ]

    if subfolders:
        for folder in subfolders:
            get_files(folder, files, name_filter)

    return files


if __name__ == '__main__':
    get_folder_path()