import os
from openpyxl import Workbook


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


def save_excel(photo_data: list, folder_path):
    # create excel workbook
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "File Path"
    sheet.column_dimensions['A'].width = 70

    sheet["B1"] = "Date"
    sheet.column_dimensions['B'].width = 40

    sheet["C1"] = "Size"
    sheet.column_dimensions['C'].width = 40

    sheet["D1"] = "Camera"
    sheet.column_dimensions['D'].width = 30

    sheet["E1"] = "Focal Length"
    sheet.column_dimensions['E'].width = 30

    sheet["F1"] = "ISO"

    for index, data in enumerate(photo_data):
        row = index + 3

        sheet[f"A{row}"] = data["file_path"]
        sheet[f"C{row}"] = f"{data['image_size'][0]}x{data['image_size'][1]}"
        sheet[f"F{row}"] = data["ISOSpeedRatings"]
        sheet[f"B{row}"] = data["DateTime"]
        sheet[f"D{row}"] = data["Model"]
        sheet[f"E{row}"] = data["FocalLength"]

    workbook.save(os.path.join(folder_path, "data.xlsx"))


if __name__ == '__main__':
    get_folder_path()