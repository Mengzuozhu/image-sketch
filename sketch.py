# -*- coding: UTF-8 -*-
import cv2
from PIL import Image, ImageOps, ImageFilter

# 次数越多，素描阴影效果越强
blur_count_for_shadow = 10


def sketch_image(in_file, out_file):
    """
    素描图片
    :param in_file:
    :param out_file:
    """
    image: Image.Image = Image.open(in_file).convert('L')
    out_image = image.copy()
    invert_image = ImageOps.invert(image.copy())
    invert_image = blur_image(invert_image, blur_count_for_shadow)
    width = int(image.width)
    for x in range(width):
        for y in range(image.height):
            raw_pixel = image.getpixel((x, y))
            invert_pixel = invert_image.getpixel((x, y))
            out_pixel = min(int(raw_pixel * 255 / (256 - invert_pixel)), 255)
            out_image.putpixel((x, y), out_pixel)
    # out_image.show()
    out_image.save(out_file)


def sketch_cv(in_file, out_file):
    image_read = cv2.imread(in_file)
    image_gray = cv2.cvtColor(image_read, cv2.COLOR_RGB2GRAY)
    image_blur = cv2.GaussianBlur(image_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
    out_image = cv2.divide(image_gray, image_blur, scale=255)
    cv2.imwrite(out_file, out_image)


def blur_image(image, count):
    """
    模糊滤镜
    :param image:
    :param count:
    :return:
    """
    for i in range(count):
        image = image.filter(ImageFilter.BLUR)
    return image


if __name__ == '__main__':
    file = 'demo.jpg'
    sketch_image(file, "out/" + file)
    sketch_cv(file, "out/" + "cv_" + file)
