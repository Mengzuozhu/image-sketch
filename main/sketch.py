# -*- coding: UTF-8 -*-

from PIL import Image, ImageOps, ImageFilter

from handler import StripeHandler

SCALE = 255
# 值越大，素描阴影效果越强
BLUR_COUNT_FOR_SHADOW = 10
# 原始图片比例
RAW_X_RANGE = [0, 0.5]
RAW_Y_RANGE = [0, 1]


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
    merge_out = StripeHandler.stripe(in_image, rgb_out)
    # merge_out = merge_raw(in_image, rgb_out)
    merge_out.save(out_file)


def merge_raw(raw_image: Image.Image, out_image: Image.Image):
    x_begin = int(raw_image.width * RAW_X_RANGE[0])
    x_end = int(raw_image.width * RAW_X_RANGE[1])
    y_begin = int(raw_image.height * RAW_Y_RANGE[0])
    y_end = int(raw_image.height * RAW_Y_RANGE[1])
    for x in range(x_begin, x_end):
        for y in range(y_begin, y_end):
            raw_pixel = raw_image.getpixel((x, y))
            out_image.putpixel((x, y), raw_pixel)
    return out_image


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
    file = '2.jpg'
    out = 'out/2.png'
    sketch_image(file, out)
