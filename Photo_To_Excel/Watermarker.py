from utilities.file_utils import get_folder_path, get_files
from utilities.watermarker_utils import create_thumbnails


def main():
    root_folder = get_folder_path()
    watermark_text = input("Your text:")

    images = get_files(root_folder, name_filter=".jpg")
    if not images:
        print(f"Couldn't find images in folder: {root_folder}")
        return

    create_thumbnails(images, watermark_text)



if __name__ == '__main__':
    main()