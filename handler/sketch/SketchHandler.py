# -*- coding: UTF-8 -*-

from PIL import Image, ImageOps, ImageFilter

from handler import StripeHandler, RatioHandler

SCALE = 255
# 值越大，素描阴影效果越强
BLUR_COUNT_FOR_SHADOW = 10


def sketch_image(in_file):
    """
    素描图片
    :param in_file:
    """
    in_image = Image.open(in_file)
    gray = in_image.convert('L')
    image: Image.Image = gray.copy()
    out_image = image.copy()
    invert_image = ImageOps.invert(image.copy())
    blur_img = blur_image(invert_image, BLUR_COUNT_FOR_SHADOW)
    for x in range(image.width):
        for y in range(image.height):
            raw_pixel = image.getpixel((x, y))
            invert_pixel = blur_img.getpixel((x, y))
            out_pixel = min(int(raw_pixel * SCALE / (256 - invert_pixel)), SCALE)
            out_image.putpixel((x, y), out_pixel)
    rgb_out = out_image.convert("RGB")
    # merge_out = StripeHandler.stripe(in_image, rgb_out)
    merge_out = RatioHandler.process(in_image, rgb_out)
    return merge_out


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
    file = '../../in/demo.jpg'
    out = '../../out/demo.png'
    res = sketch_image(file)
    res.save(out)
