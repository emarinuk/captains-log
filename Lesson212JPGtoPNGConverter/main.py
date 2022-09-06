import os

from PIL import Image, ImageFilter
from os import listdir

folder_path = input("Please enter the name of the folder containing the images: ")
image_count = 0


def replace_name(name):
    if images.endswith(".jpg"):
        my_new_name = str(name).replace(".jpg", ".png")
    else:
        my_new_name = str(name).replace(".jpeg", ".png")
    return str(my_new_name)


for images in os.listdir(folder_path):
    if images.endswith(".jpg") or images.endswith(".jpeg"):
        image_count += 1

print(f"There are {image_count} JPEG images in  the folder")
proceed = input("Do you want to convert the images to PNG? [yes,no,auto] ")

exit_loop = False
while not exit_loop:
    if proceed == "yes":
        for images in os.listdir(folder_path):
            if images.endswith(".jpg") or images.endswith(".jpeg"):
                while True:
                    consent = input(f"Do you want to convert {images} to PNG? [yes,no] ")
                    if consent == "no":
                        print(f"{images} not converted.")
                        break
                    elif consent == "yes":
                        image = Image.open(folder_path + "\\" + images)
                        new_name = replace_name(images)
                        image.save(folder_path + "\\" + new_name, "png")
                        print(f"{images} converted to {new_name}.")
                        break
                    else:
                        pass

        exit_loop = True
    elif proceed == "auto":
        for images in os.listdir(folder_path):
            if images.endswith(".jpg") or images.endswith(".jpeg"):
                image = Image.open(folder_path + "\\" + images)
                new_name = replace_name(images)
                image.save(folder_path + "\\" + new_name, "png")
        exit_loop = True
    elif proceed == "no":
        exit_loop = True
    else:
        exit_loop = True
