from PIL import Image, ExifTags


def get_photo_data(file_list: list):

    data_list = []

    for photo_file in file_list:
        img = Image.open(photo_file)
        image_size = img.size

        # get exif data
        exif_data = img._getexif()
        if not exif_data:
            continue

        photo_dict = {"file_path": photo_file, "image_size": image_size}

        # get data from exif tags
        for key, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(key)

            if tag_name == "ISOSpeedRatings":
                photo_dict["ISOSpeedRatings"] = value

            elif tag_name == "DateTime":
                photo_dict["DateTime"] = value

            elif tag_name == "Model":
                photo_dict["Model"] = value

            elif tag_name == "FocalLength":
                photo_dict["FocalLength"] = value

        data_list.append(photo_dict)

    return data_list