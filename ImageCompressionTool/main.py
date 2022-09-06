import os.path
from PIL import Image
import math


def is_jpg(path):
    if path.lower().endswith(('.jpg', '.jpeg')):
        return True
    else:
        return False


def compress_img(image_name, new_size_ratio=1, quality=20):
    img = Image.open(image_name)
    try:
        img.save(image_name, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(image_name, quality=quality, optimize=True)


def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        else:
            if is_jpg(it.path):
                my_image = Image.open(it.path)
                my_old_size = math.ceil(it.stat().st_size / 1024)
                if my_old_size > 500:
                    print(f"Compressing image: {it.path}")
                    compress_img(it.path, 1, 40)
                    my_new_size = math.ceil(it.stat().st_size / 1024)


cwd = os.getcwd()
print("Which is the root directory that you want to compress? ")
new_dir = input(f"<ENTER> will use the current one [{cwd}]")

if new_dir == "":
    new_dir = cwd
else:
    if not os.path.isdir(new_dir):
        print("Wrong answer")

listdirs(new_dir)
