from PIL import Image, ImageDraw, ImageFont
import os


def create_thumbnails(image_list: list, watermark_text: str):
    photo_folder = os.path.dirname(image_list[0])
    destination_folder = os.path.join(photo_folder, "_watermarked")
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for photo_file in image_list:
        img = Image.open(photo_file)

        # resize image
        img.thumbnail((500, 500))

        # create watermark on image
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("arial.ttf", 90)

        draw.text((0, 120), watermark_text, fill=(255, 0, 0), font=font)

        # save image to destionation
        dest_file_name = os.path.join(destination_folder, os.path.basename(photo_file))
        img.save(dest_file_name)