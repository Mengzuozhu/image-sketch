# -*- coding: UTF-8 -*-
import cv2
from PIL import Image, ImageOps, ImageFilter

SCALE = 255
# 值越大，素描阴影效果越强
BLUR_COUNT_FOR_SHADOW = 10
# 必须为正奇数
KSIZE_FOR_SHADOW = 31


def sketch_image(in_file, out_file):
    """
    素描图片
    :param in_file:
    :param out_file:
    """
    in_image = Image.open(in_file)
    image: Image.Image = in_image.convert('L')
    out_image = image.copy()
    invert_image = ImageOps.invert(image.copy())
    invert_image = blur_image(invert_image, BLUR_COUNT_FOR_SHADOW)
    for x in range(image.width):
        for y in range(image.height):
            raw_pixel = image.getpixel((x, y))
            invert_pixel = invert_image.getpixel((x, y))
            out_pixel = min(int(raw_pixel * SCALE / (256 - invert_pixel)), SCALE)
            out_image.putpixel((x, y), out_pixel)
    rgb_out = out_image.convert("RGB")
    merge_out = merge(in_image, rgb_out)
    merge_out.save(out_file)


def merge(raw_image, image2):
    out_image = image2.copy()
    x_begin = int(raw_image.width / 2)
    x_end = raw_image.width
    y_begin = int(raw_image.height / 2)
    y_end = int(raw_image.height)
    for x in range(x_begin, x_end, 1):
        for y in range(y_begin, y_end, 1):
            raw_pixel = raw_image.getpixel((x, y))
            out_image.putpixel((x, y), raw_pixel)
    return out_image


def sketch_cv(in_file, out_file):
    image_read = cv2.imread(in_file)
    image_gray = cv2.cvtColor(image_read, cv2.COLOR_RGB2GRAY)
    image_blur = cv2.GaussianBlur(image_gray, ksize=(KSIZE_FOR_SHADOW, KSIZE_FOR_SHADOW), sigmaX=0, sigmaY=0)
    out_image = cv2.divide(image_gray, image_blur, scale=SCALE)
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
    # sketch_cv(file, "out/" + "cv_" + file)
