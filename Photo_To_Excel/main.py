from utilities.file_utils import get_folder_path, get_files
from utilities.photo_data import get_photo_data


def main():
    # folder_path = get_folder_path()
    # todo REMOVE THIS!
    folder_path = r"C:\Work\_PythonSuli\pycore-211106\photos"

    # get all .jpg files from folder
    photo_files = get_files(folder_path, name_filter=".jpg")

    if not photo_files:
        print(f"I couldn't find any photos in this folder: {folder_path}")
        return

    # send files to photo_data
    photo_data_list = get_photo_data(photo_files)

    # save excel file


if __name__ == '__main__':
    main()