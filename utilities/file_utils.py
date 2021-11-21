import os


def get_files(root_folder: str, files=[], name_filter=None):
    assert os.path.exists(root_folder), f"Folder does not exist: {root_folder}"

    folder_content = os.listdir(root_folder)

    # list comprehension
    all_files = [
        os.path.join(root_folder, i) for i in folder_content  # loop function
        if os.path.isfile(os.path.join(root_folder, i))  # condition
    ]




if __name__ == '__main__':
    get_files(r"C:\Work\_PythonSuli\pycore-211106")